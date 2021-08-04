# habitica_scripts
Some habitica scripts I'd made.

They are based in https://github.com/DrStrangepork/habitica-scripts

# Get tags

Creates a json file with each tag and their ID.

Helpful for the script to replace tags.

# Replace tags

It's needed to add

- `-u [USER-ID]`
- `-k [USER-KEY]`

**The Kustom options:**
- `-d [TAG-ID]` The tag you'll like to delete from the tasks.
- `-a [TAG-ID]` The tag you'll like to add to the tasks.
- `-t [TASK-ID]` The task ID that you want to tag, untag or replace the tag.

**The posibilities**
- If you set the `delete-tag` and `add-tag` options without a `task-id`, it will replace the tag in all your tasks.
- If you set only the `delete-tag` option without a `task-id`, it will delete the tag in all your tasks.
- If you set only the `add-tag` option without a `task-id`, it will not do anything.
- if you set the `delete-tag` and the `task-id`, it will delete the tag from the task.
- if you set the `add-tag` and the `task-id`, it will add the tag to the task.
- it you set the `delete-tag`, `add-tag` and the `task-id`, it will replace the tag in the task.
- if you don't set anything, it will gives a tag (it must exist) for every task belonging to a challenge and another tag (must exist too) for every personal task. This is my  way to organize my tasks. It also deletes the wrong tags, ex. the tasks of a finished challenge. **Important** Replace the `cTag` variable with the "challenge" tag and the `pTag` variable with the "personal" tag on the python file.



