# SPDX-FileCopyrightText: 2023 Helge
# SPDX-FileCopyrightText: 2024 helge
#
# SPDX-License-Identifier: MIT

import nh3


def print_activity(activity):
    if "type" in activity:
        print(f"Type: {activity['type']:10}, Id: {activity.get('id')}")
        print()

    if "object" in activity and isinstance(activity["object"], dict):
        obj = activity["object"]

        print_object(obj, indent="    ")


def print_object(obj, indent=""):
    if "type" in obj:
        print(f"{indent}Type: {obj['type']}")
        print()

    if "name" in obj and obj["name"]:
        print(f"{indent}Name: {obj['name']}")
        print()
    if "summary" in obj and obj["summary"]:
        print(f"{indent}Summary")
        print(indent + nh3.clean(obj["summary"], tags=[], strip=True))
        print()

    if "content" in obj and obj["content"]:
        print(f"{indent}Content")
        print(indent + nh3.clean(obj["content"], tags=[], strip=True))
        print()
