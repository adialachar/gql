from .schema import schema


def getProfile(email):


    print("HELLO IM HERE YOU SEEEEEEE")


    query = """
    query getProfile($email: String){
            profile(email:$email){
                firstName,
                lastName,
                school,
                levelOfStudy,
                graduationYear,
                major,
                gender,
                genderOther,
                dateOfBirth,
                race,
                raceOther,
                phoneNumber,
                shirtSize,
                dietaryRestrictions,
                linkedin,
                github,
                resume,
                conductBox,
                shareBox
                
                

            }
        }
        """

    return schema.execute(query, variables={'email':email},)


def getUserAndProfile(email):

    query = """
        query getUser($email: String){
        user(email: $email){
    
                    password
                }
        }
            """

    return schema.execute(query, variables={'email':email},)



# def getAllUsersAndProfiles():
#
#     query = """
#         query{
#         profiles{
#             user{
#                     email,
#                     password
#                 }
#                 firstName,
#                 lastName
#                 school,
#                 levelOfStudy,
#                 graduationYear,
#                 major,
#                 gender,
#                 genderOther,
#                 dateOfBirth,
#                 race,
#                 raceOther,
#                 phoneNumber,
#                 shirtSize,
#                 dietaryRestrictions,
#                 linkedin,
#                 github,
#                 additionalLink,
#                 learnOrGain,
#                 resume,
#                 conductBox,
#                 shareBox
#
#             }
#
#         }
#             """
#
#
#     return schema.execute(query)