ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ],
}

def countFriends(dictionary, key, new_key):
  friends_count = 0
  for friends in dictionary[key]:
    friends_count += 1
  # print(friends_count)
  new_dictionary = dictionary
  new_dictionary[new_key] = friends_count
  print(new_dictionary)
  return new_dictionary
countFriends(ramit, 'friends', 'friends_count')