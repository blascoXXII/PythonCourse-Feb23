import src.questions as questions
import random
import pickle

class Player():
    
    def __init__(self, name):
        self.name = name
        self.preguntas_contestadas = 0
        self.preguntas_acertadas = 0
        
    def __str__(self):
        return self.name
    
    def add_question(self):
        self.preguntas_contestadas += 1
        
    def right_answer(self):
        self.preguntas_acertadas +=1
        self.add_question()
        
    def wrong_answer(self):
        self.add_question()

class Game():
    
    def __init__(self, players_list):
        
        self.question_set = []
        self.players = {}
        
        for player in players_list:
           self.players[player.name] = player
    
    def add_new_questions(self, questions):
        self.question_set += questions
           
    def play_round(self):
        
        if len(self.question_set) >= len(self.players):
        
            for player in self.players:
                
                print(f"Turno del jugador {player}")
                print("")
                
                numero_pregunta = random.randint(0,len(self.question_set)-1)
                pregunta = self.question_set.pop(numero_pregunta)
                print(pregunta)
                
                respuesta = input(f"{player} indique la respuesta correcta: ")
                
                if pregunta.validate_answer(respuesta):
                    print("La respuesta es correcta")
                    self.players[player].right_answer()
                    
                else:
                    print("Respuesta erronea")
                    self.players[player].wrong_answer()
                    
        else:
            print ("Not enough questions to play another round")
            
        print("")
        print("")
           
    def get_winner(self):
        
        winner = ""
        max_points = 0
        
        for player in self.players.values():
            
            if player.preguntas_acertadas > max_points:
                winner = player.name
                max_points = player.preguntas_acertadas
                
            elif player.preguntas_acertadas == max_points:
                winner += f" and {player.name}"
                
        print(f"Winner: {winner}\nPoints: {max_points}")
        
    def save_game(self, path):
        
        with open(path, "wb"):
            pickle.dump(path)


def load_game(path):
    
    with open(path, "rb"):
        g = pickle.load(path)
        
    return g
           
            
        
        
if __name__ == "__main__":
    
    #Set questions
    q1 = questions.Question("How much is 1+1", "2","1","3","4")  
    q2 = questions.Question("First letter of the alphabet","a","b","c","d")
    
    #Set players
    p1 = Player("Paco")
    p2 = Player("Maria")
    
    #Initialize game
    game = Game([p1, p2])
    game.add_new_questions([q1, q2])
    
    game.play_round()
    game.play_round()
    
    game.get_winner()
    
         

