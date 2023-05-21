def vinc(mode):
    print("(version_increase): Incrementing program version in version.txt")
    print("(version_increase): Selected mode is " + mode)
    try:
        v_file = open("version.txt", "r")
        print("(version_increase): version.txt loaded")
    except:
        print("(version_increase): version.txt does not exist!")
        return
    version = v_file.readline()
    v_file.close()
    print("(version_increase): Previous version is "  + version)
    version = version.split(".")
    print(version)
    if mode in"Major" "major" "Majour" "majour":
        version[0] = str(int(version[0]) + 1)
        version[1] = "0"
        version[2] = "0"
    if mode in "Medium" "medium":
        version[1] = str(int(version[1]) + 1)
        version[2] = "0"
    if mode in "Minor" "minor":
        version[2] = str(int(version[2]) + 1)
        print("Yes")
    version = '.'.join(version)
    print("(version_increase): New version is " + version)
    v_file = open("version.txt", "w")
    v_file.write(version)
    v_file.close()
    print("(version_increase): Returning to main")
