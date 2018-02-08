import os.path

if __name__ == '__main__':
  tool_dir = r"X:\tools"
  if not os.path.exists(tool_dir):
    input('"{0}" not found!\nimport of dism_wizzard may not work\npress enter to continue: '.format(tool_dir))
  import sys
  sys.path.append(tool_dir)
  import dism_wizzard
  dism_wizzard.main()
