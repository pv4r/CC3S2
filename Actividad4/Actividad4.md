# Initialize the repository

![[Pasted image 20250404113746.png]]
# Create a new file

![[Pasted image 20250404121205.png]]
# Check the status of the repository

![[Pasted image 20250404121304.png]]
# Track the new file

![[Pasted image 20250404131246.png]]
# Save the changes

![[Pasted image 20250404133742.png]]

# Commit tree

![[Pasted image 20250404134029.png]]
## What is the output for this command:

```bash
git log --graph --pretty=format:'%x09 %h %ar ("%an") %s'
```

![[Pasted image 20250404134116.png]]
# Practice with the git log command

![[Pasted image 20250404134728.png]]

![[Pasted image 20250404134814.png]]

![[Pasted image 20250404134853.png]]

# List the branches

![[Pasted image 20250404135050.png]]

# Create a new branch

![[Pasted image 20250404135154.png]]

# Switch between branches

![[Pasted image 20250404135853.png]]
Equivalent,

```bash
git switch feature/new-feature
```

## Create a new branch and switch to it

![[Pasted image 20250404185521.png]]
Equivalent,

```bash
git switch -c feature/another-new-feature 
```

# Merge branches

![[Pasted image 20250404193836.png]]

# Delete the unnecessary branch

![[Pasted image 20250404194004.png]]

# Exercises

## Exercise 1: Advanced branch management and conflict resolution

1. Create a new branch for a feature
		![[Pasted image 20250404234929.png]]
2. Modify files in the new branch
	- Edit the `main.py` file to include an additional function:
			![[Pasted image 20250404235419.png]]
	- Add and commit these changes to the feature/advanced-feature branch:
			![[Pasted image 20250405002854.png]]
3. Simulate parallel development on the main branch:
		![[Pasted image 20250405003324.png]]
4. Try to merge the `feature/advance-feature` branch into `main`:
		![[Pasted image 20250405003650.png]]
5. Fix the merge conflict:
		![[Pasted image 20250405005919.png]]		
		![[Pasted image 20250405005953.png]]
		![[Pasted image 20250405010040.png]]
6. Delete the merged branch:
		![[Pasted image 20250405010201.png]]

## Exercise 2: Exploring and manipulating commit history

1. View detailed commit history
		![[Pasted image 20250405083011.png]]
		![[Pasted image 20250405083044.png]]
2. Filter commits by author:
		![[Pasted image 20250405083313.png]]
3. Revert a commit:
		![[Pasted image 20250405093312.png]]
		![[Pasted image 20250405093521.png]]
4. Interactive Rebase:
		![[Pasted image 20250405113613.png]]
		![[Pasted image 20250405113708.png]]
	- Fix conflict:
		![[Pasted image 20250405113911.png]]
		![[Pasted image 20250405113945.png]]
		![[Pasted image 20250405114049.png]]
		![[Pasted image 20250405114120.png]]
	- Finally,
		![[Pasted image 20250405114215.png]]
5. Graphical display of history:
		![[Pasted image 20250405114405.png]]

## Exercise 3: Creation and management of branches from specific commits
1. Create a new branch from a specific commit:
	- Check the commit history:
		![[Pasted image 20250405121724.png]]
	- Create a new branch `bugfix/rollback feature` from `e032ab1`:
		![[Pasted image 20250405122144.png]]
2. Modify and confirm changes in the new branch:
		![[Pasted image 20250405122747.png]]
		![[Pasted image 20250405122822.png]]
3. Merge the changes into the main branch:
		![[Pasted image 20250405123424.png]]
		![[Pasted image 20250405123504.png]]
		![[Pasted image 20250405123532.png]]
		![[Pasted image 20250405123807.png]]
4. Explore the history after the merge:
		![[Pasted image 20250405123931.png]]
5. Delete the branch `bugfix/rollback-feature`:
		![[Pasted image 20250405124616.png]]
## Exercise 4: Manipulation and restoration of commits using git reset and git restore

1. Edit the `main.py` file to introduce a new change:
		![[Pasted image 20250405125132.png]]
2. Use `git reset` for undo the commit:
		![[Pasted image 20250405125407.png]]
3. Use `git restore` for undo uncommitted changes:
		![[Pasted image 20250405125659.png]]
		![[Pasted image 20250405125734.png]]
## Exercise 5: Collaborative work and handling of Pull Requests

1. Create a new remote repository:
		![[Pasted image 20250405143447.png]]
		![[Pasted image 20250405144450.png]]
2. Create a new branch for feature development:
		![[Pasted image 20250405151422.png]]
3. Make changes and push the branch to the remote repository:
	- Make changes to the project files and commit them
			![[Pasted image 20250405151842.png]]
	- Push the branch to the remote repository
			![[Pasted image 20250405152632.png]]
	- Use `set-url`, because SSH verification is required to perform a push
			![[Pasted image 20250405152921.png]]
4. Open a pull request:
		![[Pasted image 20250405154115.png]]
5. Review and merge the pull request:
		![[Pasted image 20250405154525.png]]
		![[Pasted image 20250405154615.png]]
		![[Pasted image 20250405154845.png]]
		![[Pasted image 20250405155003.png]]
		![[Pasted image 20250405155048.png]]
		![[Pasted image 20250405160016.png]]
6. Delete remote and local branch:
		![[Pasted image 20250405160309.png]]
## Exercise 6: Cherry Picking & Git Stash

1. Make changes to `main.py` file and commit them:
		![[Pasted image 20250405161314.png]]
2. Create a new branch and apply the specific commit:
		![[Pasted image 20250405161651.png]]
3. Temporarily save uncommitted changes:
		![[Pasted image 20250405161836.png]]
4. Apply the saved changes:
		![[Pasted image 20250405162034.png]]
		![[Pasted image 20250405162238.png]]
		![[Pasted image 20250405162311.png]]
5. View git log:
		![[Pasted image 20250405162415.png]]