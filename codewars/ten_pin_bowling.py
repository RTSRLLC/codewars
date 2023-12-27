def bowling_score(frames):
    bowl_frames = frames.split()
    bowl_frame_types = []
    for num in bowl_frames:
        print(list(num))
        if '/' in list(num):
            bowl_frame_types.append(('spare', 10, num))
        elif 'X' in list(num) and any('X' not in x for x in bowl_frames):
            bowl_frame_types.append(('strike', 10, num))
        else:
            bowl_frame_types.append(('regular', sum(int(x) for x in num)), num)
        print(bowl_frame_types)
    print(bowl_frame_types)
    return


# a = bowling_score('11 11 11 11 11 11 11 11 11 11')  # , 20)
print('*' * 50)
# b = bowling_score('X X X X X X X X X XXX')  # , 300)
print('*' * 50)
c = bowling_score('X X 9/ 80 X X 90 8/ 7/ 44')

"""
Bowling scoring can seem complex at first, but it's straightforward once you break it down. Here's a simplified explanation:

1. **Frames:**
   - A game of bowling consists of 10 frames.
   - In each frame, the player has two chances to knock down 10 pins.

2. **Scoring:**
   - **Regular Score:** If you knock down all 10 pins in two tries, you score the number of pins knocked down.
   - **Spare:** If you knock down all 10 pins in two tries (a spare), you score 10 plus the number of pins knocked down on your next roll.
   - **Strike:** If you knock down all 10 pins on your first try (a strike), you score 10 plus the number of pins knocked down in your next two rolls.

3. **Tenth Frame Special:**
   - In the 10th frame, if you bowl a spare or strike, you get extra rolls (one for a spare, two for a strike) to complete the scoring for the frame.

4. **Maximum Score:**
   - The maximum score in a single game of bowling is 300, achieved by rolling 12 strikes in a row (one for each frame plus two additional strikes in the tenth frame).

5. **Keeping Track:**
   - The score for each frame is cumulative. You add the score of each frame to the total score from the previous frames.

In essence, you're trying to knock down pins and score points, with bonuses (spares and strikes) giving you the chance to add extra pins to your score. The key is understanding how the bonuses work to maximize your score.

"""
