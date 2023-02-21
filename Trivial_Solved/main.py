import src.questions as questions
import src.game as game


    
 #Set players
p1 = game.Player("Paco")
p2 = game.Player("Maria")

#Initialize game
main_game = game.Game([p1, p2])
main_game.add_new_questions(questions.get_questions_from_file(\
                            r"C:\Users\Blasco\Desktop\CursPython\Day5\Trivial_Solved\TriviaQuestions.csv"))

main_game.play_round()
main_game.play_round()

main_game.get_winner()