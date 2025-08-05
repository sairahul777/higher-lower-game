import random
logo='''
  _   _ ___ ____ _   _ _____ ____  
 | | | |_ _/ ___| | | | ____|  _ \ 
 | |_| || | |  _| |_| |  _| | |_) |
 |  _  || | |_| |  _  | |___|  _ < 
 |_| |_|___\____|_| |_|_____|_| \_\ 
  _     _____        _______ ____  
 | |   / _ \ \      / / ____|  _ \ 
 | |  | | | \ \ /\ / /|  _| | |_) |
 | |__| |_| |\ V  V / | |___|  _ < 
 |_____\___/  \_/\_/  |_____|_| \_\ 
 '''
versus_logo='''              
 __   _____   
 \ \ / / __|  
  \ V /\__ \_ 
   \_/ |___(_)
              
'''



print(logo)




data = [
    {'name': 'Cristiano Ronaldo', 'follower_count': 630, 'description': 'Footballer', 'country': 'Portugal'},
    {'name': 'Lionel Messi', 'follower_count': 520, 'description': 'Footballer', 'country': 'Argentina'},
    {'name': 'Selena Gomez', 'follower_count': 430, 'description': 'Singer and actress', 'country': 'United States'},
    {'name': 'Kylie Jenner', 'follower_count': 410, 'description': 'Reality TV star and businesswoman', 'country': 'United States'},
    {'name': 'Dwayne Johnson', 'follower_count': 395, 'description': 'Actor and former wrestler', 'country': 'United States'},
    {'name': 'Ariana Grande', 'follower_count': 380, 'description': 'Singer and actress', 'country': 'United States'},
    {'name': 'Kim Kardashian', 'follower_count': 360, 'description': 'Reality TV star and businesswoman', 'country': 'United States'},
    {'name': 'Beyoncé', 'follower_count': 320, 'description': 'Singer and performer', 'country': 'United States'},
    {'name': 'Virat Kohli', 'follower_count': 275, 'description': 'Cricketer', 'country': 'India'},
    {'name': 'Justin Bieber', 'follower_count': 290, 'description': 'Singer', 'country': 'Canada'},
    {'name': 'Taylor Swift', 'follower_count': 270, 'description': 'Singer-songwriter', 'country': 'United States'},
    {'name': 'Neymar Jr', 'follower_count': 260, 'description': 'Footballer', 'country': 'Brazil'},
    {'name': 'Jennifer Lopez', 'follower_count': 250, 'description': 'Singer and actress', 'country': 'United States'},
    {'name': 'Kendall Jenner', 'follower_count': 280, 'description': 'Model and TV personality', 'country': 'United States'},
    {'name': 'Nicki Minaj', 'follower_count': 240, 'description': 'Rapper and singer', 'country': 'United States'},
    {'name': 'Khloé Kardashian', 'follower_count': 220, 'description': 'Reality TV star', 'country': 'United States'},
    {'name': 'Miley Cyrus', 'follower_count': 210, 'description': 'Singer and actress', 'country': 'United States'},
    {'name': 'Shakira', 'follower_count': 200, 'description': 'Singer and performer', 'country': 'Colombia'},
    {'name': 'Drake', 'follower_count': 195, 'description': 'Rapper and singer', 'country': 'Canada'},
    {'name': 'Zendaya', 'follower_count': 190, 'description': 'Actress and singer', 'country': 'United States'},
    {'name': 'LeBron James', 'follower_count': 180, 'description': 'Basketball player', 'country': 'United States'},
    {'name': 'Chris Hemsworth', 'follower_count': 160, 'description': 'Actor', 'country': 'Australia'},
    {'name': 'Emma Watson', 'follower_count': 155, 'description': 'Actress and activist', 'country': 'United Kingdom'},
    {'name': 'Rihanna', 'follower_count': 150, 'description': 'Singer and entrepreneur', 'country': 'Barbados'},
    {'name': 'Katy Perry', 'follower_count': 140, 'description': 'Singer', 'country': 'United States'},
    {'name': 'Gal Gadot', 'follower_count': 130, 'description': 'Actress', 'country': 'Israel'},
    {'name': 'Zlatan Ibrahimović', 'follower_count': 120, 'description': 'Footballer', 'country': 'Sweden'},
    {'name': 'Billie Eilish', 'follower_count': 110, 'description': 'Singer', 'country': 'United States'},
    {'name': 'Shah Rukh Khan', 'follower_count': 95, 'description': 'Actor', 'country': 'India'},
    {'name': 'Tom Holland', 'follower_count': 100, 'description': 'Actor', 'country': 'United Kingdom'}
]
def gen_random():
    random_val=random.randint(0,29)
    return random_val

def ran_celeb():
    random_celeb=(data[gen_random()]) 
    return random_celeb

should_continue=True
count=0
while should_continue:
    celeb_a=ran_celeb()
    celeb_b=ran_celeb()
    a=celeb_a['follower_count']
    b=celeb_b['follower_count']
    print(f"current score is: {count}")
    print(celeb_a['name'],"is a",celeb_a['description'],"and from",celeb_a['country'])
    print(versus_logo)
    print(celeb_b['name'],"is a",celeb_b['description'],"and from",celeb_b['country'])
    guess=input("who has more followers. type 'A' or 'B': ").lower()
    
    if guess=='a':
        choice=a
        opponent=b
    elif guess=='b':
        choice=b
        opponent=a
    
    
    
    if choice==opponent:
        opponent=ran_celeb()
        
    if choice>opponent:
      print("\n"*3)
      count+=1
      continue
    elif choice<opponent:
      print("you guessed it wrong.")
      print(f"your final score is: {count}")
      print("Better luck next time!👍")
      should_continue=False
  

    
    



