import IGram

insta=IGram.IGHandel("vaibhav_pandey_2005") #Instagram Handle

#Get the user NAME
username=insta.Name()
print(username)

#Get Alternate Name
alt_name=insta.AlternateName()
print(alt_name)

#Get Followers
followers=insta.Followers()
print(followers)

#Get Following
following=insta.Following()
print(following)

#Get Posts
posts=insta.Posts()
print(posts)

#Get profile image link
img=insta.ProfileImage()
print(img)

#Get Description
desc=insta.Description()
print(desc)