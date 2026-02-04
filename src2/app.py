from App import screen


main_menu: screen = screen()

def SetupScreens():
    main_menu.lines.append({"line": f"", "end": f"\n"})
    main_menu.lines.append({"line": f"What would you like to do?", "end": f"\n"})
    main_menu.lines.append({"line": f"  1) Create Project", "end": f"\n"})
    main_menu.lines.append({"line": f"  2) Exit", "end": f"\n"})
    main_menu.lines.append({"line": f"", "end": f"\n"})
    main_menu.lines.append({"line": f"#> ", "end": f""})


def AppMainFunction():
    SetupScreens()

    main_menu.print()


if __name__ == "__main__":
    AppMainFunction()