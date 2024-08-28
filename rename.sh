#!bash

NEW_NAME=$1

find desk \
  -name "*sunrise*" \
  -exec bash -c "echo {} | sed 's/sunrise/$NEW_NAME/' | xargs mv {}" \; 2> /dev/null

CAPITAL_NAME="${NEW_NAME^}"

# Rename contents
find desk \
	-type f \
 	-exec sed -i '' "s/sunrise/$NEW_NAME/g" {} \; \
  -exec sed -i '' "s/Sunrise/$CAPITAL_NAME/g" {} \;
  
