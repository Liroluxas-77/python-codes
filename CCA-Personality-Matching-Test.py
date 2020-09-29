prnt("Title of program: CCA Matching Personality test")
print()
print("Welcome to DHS! Please answer the following questions honestly and we'll suggest a CCA for you!")
print("Please respond with a number 1 - 5, where 1 is strongly disagree and 5 is strongly agree.")
print(

sports1 = input("I enjoy playing ball sports.")

outdoor1 = input("I love to go camping.")

music1 = input("I love to listen to music.")

club1 = input("I like to do tech stuff or draw.")

sports2 = input("I know how to play a sport.")

outdoor2 = input("I pass my napfa running test with flying colours.")

music2 = input("I like to perform on stage.")

club2 = input("I prefer to work in groups and having my own time to myself.")


sports_final = int(tech1) + int(tech2)
outdoor_final = int(outdoor1) + int(outdoor2)
music_final = int(music1)+ int(music2)
club_final = int(club1)+ int(club2)

print()

if sports_final > outdoor_final and sports_final > music_final and sports_final > club_final:
  print("You might be suitable for a sports CCA! You can take another more specific quiz at <insert link here>")
elif outdoor_final > music_final and outdoor_final > club_final:
  print("You might be stuiable for a uniformed group CCA! You can take another more specific quiz at <insert link here>")
elif music_final > club_final:
  print("You might be suitable for a performing arts CCA! You can take another more specific quiz at <insert link here>")
else:
  print("You might be suitable for a club or society! You can take another more specific quiz at <insert link here>")
