import cmd, sys
import pathlib

class FileShell(cmd.Cmd):
    intro = ""
    prompt = pathlib.Path(sys.argv[0]).resolve().as_uri().removeprefix("file:///").replace("%20", " ") + ">>"
    file = pathlib.Path(sys.argv[0]).resolve()

    def update_prompt(self):
        self.prompt = self.file.resolve().as_uri().removeprefix("file:///").replace("%20", " ") + ">"

    def do_gotoback(self, arg):
        if self.file.name != "":
            self.file = self.file.parents[0]
            self.update_prompt()
        else:
            print("EXCEPTION: cannot go back further than the root drive, do you want to visit the universe?")

    def do_prtname(self, arg):
        print(self.file.name)

    def do_goto(self, arg):
        if (self.file/arg).exists():
            self.file = (self.file/arg).resolve()
            self.update_prompt()
        else:
            print("EXCEPTION: " + (self.file/arg).resolve().as_uri().removeprefix("file:///").replace("%20", " ") + " does not exist, do want to enter Null and Void?")

    def do_gotoroot(self, arg):
        if self.file.name != "":
            self.file = pathlib.Path(self.file.root)
            self.update_prompt()

    def do_prtct(self, arg):
        if (self.file/arg).exists():
            if (self.file/arg).is_file():
                print((self.file/arg).read_text())
            else:
                print("EXCEPTION: cannot print a directory, im too lazy to implement that")
        else:
            print("EXCEPTION: " + (self.file/arg).resolve().as_uri().removeprefix("file:///").replace("%20", " ") + " does not exist")

FileShell().cmdloop()