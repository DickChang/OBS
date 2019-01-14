import urllib, time, re, os

file = open("input.txt", "r");

character = ""
for line in file:
    if "animat" in line:
        regex = re.compile("^.+\[B](.+) animat.+")
        character = regex.match(line).group(1)
        character = character.replace(" ", "_")
        if not os.path.exists(character):
            os.mkdir(character)
        print character
    elif "[IMG]" in line:
        regex1 = re.compile("^\[IMG](.+)\[\/IMG].*")
        fetch_url = regex1.match(line).group(1)

        regex2 = re.compile("^.+\/(.+\.gif).*")
        img_name = regex2.match(fetch_url).group(1)
        print fetch_url
        full_save_path = os.path.join(character, img_name)
        print "\t" + full_save_path
        if not os.path.exists(full_save_path):
            urllib.urlretrieve(fetch_url, full_save_path)
            time.sleep(1)
    else:
        print ""
        

exit(1)

