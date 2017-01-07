#The Purpose of this script is to verify the correct asset names for My organization assets to be placed in the DAM system.
#My organization requires that all assets meet specific naming conventions, often these conventions are forgotten or ignored. This script is an attempt to limit the number of errors that I  produce.
# Conventions are:
#	1.All lower case text
#	2.use of hyphens not underscore symbols.
#	3.no spaces between characters/symbols.
#   4."CompanyName" name should not be used in any part of the file name.

print ("\n\t Welcome to my Asset Naming application.\n\tThe purpose of this application is to help reduce the number of naming errors that happen in the process of adding Assets to the DAM.")


#Lets get the Asset Name as it was originally provided.
assetName_old = input("\n\n\nWhat is the Name of the asset that needs to be checked?\n\n")

print ("\nSo this is the name of the asset that needs to be check.\n\n" +assetName_old)
print ("\nLets get the name all lower case first.\n\n")

#JAN6-17 changes - case change update
assetName_lower = assetName_old.lower()

print (assetName_lower)

print ("Now we will replace characters that are not used in our naming conventions.")

#JAN6-17 This could possible be a little cleaner, for this works and I have not had the time to find the perfect cure. It replaces all the things that should not be in an Asset name for my company.
assetName_chars_replace = assetName_lower.replace('_', '-').replace(' ', '-').replace('CompanyName', '').replace('--', '-').replace('.', '-')

print (assetName_chars_replace)
