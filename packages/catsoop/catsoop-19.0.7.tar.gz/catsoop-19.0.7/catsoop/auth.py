# This file is part of CAT-SOOP
# Copyright (c) 2011-2023 by The CAT-SOOP Developers <catsoop-dev@mit.edu>
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License for more
# details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
User authentication for normal interactions
"""

import os
import importlib

from . import api
from . import loader
from . import cslog
from . import base_context

importlib.reload(base_context)


def _execfile(*args):
    fn = args[0]
    with open(fn) as f:
        c = compile(f.read(), fn, "exec")
    exec(c, *args[1:])


def get_auth_type(context):
    """
    Return the methods associated with the currently chosen authentication
    type.

    **Parameters**:

    * `context`: the context associated with this request.

    **Returns:** a dictionary containing the variables defined in the
    authentication type specified by `context['cs_auth_type']`.
    """
    auth_type = context["csm_base_context"].cs_auth_type
    return get_auth_type_by_name(context, auth_type)


def get_auth_type_by_name(context, auth_type):
    """
    Helper function.  Returns the methods associated with the given
    authentication type, regardless of which is active.

    **Parameters**:

    * `context`: the context associated with this request.
    * `auth_type`: the name of the authentication type in question.

    **Returns:** a dictionary containing the variables defined in the
    authentication type specified by `auth_type`.
    """
    fs_root = context.get("cs_fs_root", base_context.cs_fs_root)

    tail = os.path.join("__AUTH__", auth_type, "%s.py" % auth_type)
    global_loc = os.path.join(fs_root, tail)

    e = dict(context)
    if os.path.isfile(global_loc):
        _execfile(global_loc, e)
    else:
        # no valid auth type found
        raise Exception("Invalid cs_auth_type: %s" % auth_type)

    return e


def get_logged_in_user(context):
    """
    From the context, get information about the logged in user.

    If the context has an API token in it, that value will be used to determine
    who is logged in.  Otherwise, the currently-active authentication type's
    `get_logged_in_user` function is used.

    Side effect: if the user in question does not have an API token already, a
    new one is created for them.

    **Parameters:**

    * `context`: the context associated with this request

    **Returns:** a dictionary containing the information associated with the
    user who is currently logged in.  If a user is logged in, it will contain
    some subset of the keys `'username'`, `'name'`, and `'email'`.
    """
    # handle auto-login for LTI users
    lti_data = context["cs_session_data"].get("lti_data")
    doing_logout = context["cs_form"].get("loginaction", None) == "logout"
    if lti_data and not doing_logout:
        cui = lti_data.get("cs_user_info")
        context["cs_user_info"] = cui
        return cui

    # if an API token was specified, use the associated information and move on
    # this has the side-effect of renewing that token (moving back the
    # expiration time)
    api_user = api.get_logged_in_user(context)
    if api_user is not None:
        return api_user

    regular_user = get_auth_type(context)["get_logged_in_user"](context)
    return regular_user


def get_user_information(context):
    """
    Based on the context, load extra information about the user who is logged
    in.

    This method is used to load any information specified about the user in a
    course's `__USERS__` directory, or from a global log.  For example,
    course-level permissions are loaded this way.

    This function is also responsible for handling impersonation of other
    users.

    **Parameters:**

    * `context`: the context associated with this request

    **Returns:** a dictionary like that returned by `get_logged_in_user`, but
    (possibly) with additional mappings as specified in the loaded file.
    """
    return _get_user_information(
        context,
        context["cs_user_info"],
        context.get("cs_course", None),
        context["cs_username"],
    )


def _get_user_information(context, into, course, username, do_preload=False):
    if course is not None:
        if do_preload:
            loader.load_global_data(context)
            loader.do_preload(context, course, [], context)
        fname = os.path.join(  # path to user definition py file in course data
            context["cs_data_root"],
            "courses",
            context["cs_course"],
            "__USERS__",
            "%s.py" % username,
        )
    else:
        fname = os.path.join(context["cs_data_root"], "_logs", username)
    if os.path.exists(fname):
        with open(fname) as f:
            text = f.read()
        exec(text, into)
        loader.clean_builtins(into)

    if str(username) == "None":
        into["role"] = "Unauthenticated"

    # permissions handling
    if "permissions" not in into:
        if "role" not in into:
            into["role"] = context.get("cs_default_role", None)
        plist = context.get("cs_permissions", {})
        defaults = context.get("cs_default_permissions", {"view"})
        into["permissions"] = set(plist.get(into["role"], defaults))

    # impersonation
    if ("as" in context.get("cs_form", {})) and ("real_user" not in into):
        if "impersonate" not in into["permissions"]:
            return into
        into["preserve_permissions"] = context.get("cs_form", {}).get(
            "preserve_permissions", "f"
        ).lower() in {"true", "t", "1", "yes", "y"}
        old = dict(into)
        old["p"] = into["permissions"]
        context["cs_username"] = context["cs_form"]["as"]
        into["real_user"] = old
        into["username"] = into["name"] = context["cs_username"]
        into["role"] = None
        del into["permissions"]
        into = get_user_information(context)

        check_impersonate = context.get(
            "cs_impersonation_allowed", lambda old, new: True
        )
        if not check_impersonate(old, into):
            # this impersonation is not allowed; reset everything
            into = old
            context["cs_username"] = into["username"]
            del into["p"]
            del into["preserve_permissions"]

    # handle spoofed permissions
    spoofed_role = context.get("cs_form", {}).get("as_role", None)
    if spoofed_role is not None and "impersonate" in into["permissions"]:
        orig_p = into["permissions"]
        spoofed_p = plist.get(spoofed_role, defaults)
        new_p = set(spoofed_p).intersection(set(orig_p))
        for i in ("submit_all", "view_all"):
            lesser = i.split("_")[0]
            if i in orig_p and i not in new_p and lesser in spoofed_p:
                new_p.add(lesser)
        into["permissions"] = new_p
        if new_p != orig_p:
            into["role"] = spoofed_role

    cslog = context["csm_cslog"]
    if "username" in into:
        logininfo = cslog.most_recent(
            "_logininfo",
            [],
            into["username"],
            {},
        )
        logininfo = {
            k: v for k, v in logininfo.items() if k in ("username", "name", "email")
        }
        into.update(logininfo)
        extra_info = cslog.most_recent(
            "_extra_info",
            [],
            into["username"],
            {},
        )
        into.update(extra_info)

    if str(username) == "None":
        if "view" in into["permissions"]:
            into["permissions"] = ["view"]
        else:
            into["permissions"] = []
    return into
