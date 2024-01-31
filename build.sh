#!/bin/bash

# Echo commands
echo "Start building..."
echo "Cleaning previous build......"
rm -r dist
echo "Building English version......"
pyinstaller main.spec
echo "Building Chinese (Simp) version......"
pyinstaller main-zhs.spec
echo "Building Chinese (Trad) version......"
pyinstaller main-zht.spec

# Change directory
cd dist
echo "Combining files......"

# Copy everything into zht folder as zht needs extra GUI font
cp -r ./main/main ./main-zht/
# cp -r ./main/main.manifest ./main-zht/
cp -r ./main-zhs/main-zhs ./main-zht/
# cp -r ./main-zhs/main-zhs.manifest ./main-zht/

echo "Deleting redundant file......"
# Remove directories
rm -rf ./main
rm -rf ./main-zhs

# Rename directory
mv "main-zht" "CJK-character-count-vX.XX"

echo "Build done!"
echo "Press Enter to exit."

# Wait for user to press enter
read -r -s -n 1
