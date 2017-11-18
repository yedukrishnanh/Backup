import os
import shutil
import time
def backupProcess(Original_Directory, Backup_Directory):
    global loop
    before = dict(((f, None) for f in os.listdir(Backup_Directory)))  # Making list of  initial set of files to variable before
    while loop:  # Infinite loop to keep on monitoring once service is started
        time.sleep(10)  # Sleep for 10 seconds after each checking so as to reduce RAM consumption
        after = dict(((f, None) for f in os.listdir(Original_Directory)))  # Making list of  current set of files to variable after
        added = [f for f in after if not f in before]  # Listing new files by comparing list before and list after as list added

        if added:  # If added not empty                    (If there are newfiles)
            print("Found: ", added)  # Print Found
            for newfile in added:  # for every element of list added (For every new file)
                new = Original_Directory + newfile  # Adding path and name of new file to use in copy operation
                shutil.copy(new, Backup_Directory)  # Copying new file to Backup directory
                print("Copied ", newfile)  # Print copied after making backup
        before = after  # Changing list before to list after since every element in after is backed up
