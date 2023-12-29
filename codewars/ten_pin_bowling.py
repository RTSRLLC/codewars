def score_frames(frames):
    """
    Calculate the score for each frame in a game of ten-pin bowling.

    This function takes a list of frames as input and calculates the score for each frame based on the rules of
    ten-pin bowling. The frames can contain either a number of pins knocked down (e.g., '7', '9') or special
    symbols ('X' for a strike, '/' for a spare). The function returns a list of tuples, where each tuple contains
    the score, type of frame (strike, spare, or regular), and the frame itself.

    Args:
        frames (list): A list of frames representing the rolls in a game of ten-pin bowling.

    Returns:
        list: A list of tuples, where each tuple contains the score, type of frame, and the frame itself.

    Examples:
        >>> score_frames(['X', '7/', '9-', 'X', '-8', '8/', 'X', 'X', 'X', '9/7'])
        [(10, 'strike', 'X'), (10, 'spare', [7, 3]), (9, 'regular', [9, 0]), (10, 'strike', 'X'), (8, 'regular', [0, 8]), (10, 'spare', [8, 2]), (10, 'strike', 'X'), (10, 'strike', 'X'), (10, 'strike', 'X'), (9, 'spare', [9, 1])]
    """
    scoring = []
    for idx, frame in enumerate(frames):
        if idx == 9:
            print(f"final frame accessed: {frames[-1]}")
            final = scoring.append(final_frame(frames[-1]))
        elif frame == 'X':
            # ex. (10, 'strike', 10)
            scoring.append((10, 'strike', [10]))
        elif frame[1] == '/':
            # ex. (10, 'spare', [7])
            scoring.append((10, 'spare', [int(i) for i in list(frame) if i != '/']))
        else:
            # ex. (8, 'regular', [8, 0])
            print(f'frame: {frame}')
            scoring.append((int(frame[0]) + int(frame[1]), 'regular', [int(i) for i in list(frame)]))
        print(f'frame: {frame}')
    return scoring


def frame_type(frame: tuple) -> str:
    """
    Determine the type of a frame in a game of ten-pin bowling.

    This function takes a frame as input and returns the type of the frame for scoring purposes.
    The frame can be represented as a string, where the first character represents the number of pins knocked down
    and the second character represents the type of frame ('/' for a spare). The function returns the second character
    of the frame.

    Args:
        frame (str): A string representing a frame in a game of ten-pin bowling.

    Returns:
        str: The type of the frame.

    Examples:
        >>> frame_type((10, 'spare', 9))
        'spare''
        >>> frame_type((10, 'strike', 10))
        'strike'
    """
    return frame[1]


def final_frame(frame):
    """
    Determine final frame score in a game of ten-pin bowling.
    This frame can have length 2 or 3 depending on whether the player scored a strike, spare, or neither in the final
    frame. The function returns the score for each roll of the final frame.
    Args:
        frame (): a string representing the final frame in a game of ten-pin bowling.

    Returns: the score for each roll of the final frame.

    """
    final_frame = list(frame)
    print(f'final_frame: {final_frame}')
    score = 0
    out_frame = []
    for roll in final_frame:
        if roll == 'X':
            out_frame.append(10)
        elif roll == '/':
            out_frame.append(10 - out_frame[-1])
        else:
            out_frame.append(int(roll))
        print(f'out_frame: {out_frame}')
    return sum(out_frame), 'final frame', out_frame


def get_next_rolls(tup: tuple, roll: str) -> int:
    """
    Take in a tuple of the form (8, 'regular', [4, 4]) and returns the third index of the tuple, which is a list of
    the rolls in the frame. This function is used to determine the next roll(s) to add to the score of a strike or spare.
    Args:
        tup (): a tuple of the form (int, bowl roll, [rolls])
        roll (): a string representing the roll of bowl (strike, spare, regular)

    Returns: int to add to the score of a strike or spare.

    """
    if roll == 'strike':
        return sum(i for i in tup[2] if tup[1] != 'strike')
    if roll == 'spare':
        return tup[2][0]
    if roll =='regular':
        return tup[2][0]


def bowling_score(frames):
    bowl_frames = frames.split()
    scores = score_frames(bowl_frames)
    updated_scores = []
    print(scores)
    # [(10, 'strike', [10]), (10, 'strike', [10]), (10, 'spare', [9]), (8, 'regular', [8, 0]), (10, 'strike', [10]), (10, 'strike', [10]), (9, 'regular', [9, 0]), (10, 'spare', [8]), (10, 'spare', [7]), (14, 'final frame', [4, 4, 6])]
    for i, score in enumerate(scores):
        print(f"i: {i}, score: {score}")
        if i == 9:
            print(f"final frame accessed: {frames[-1]}")
            updated_scores.append(final_frame(score[-1]))
        if score[1] == 'strike':
            if scores[i + 1][1] == 'strike':
                updated_scores.append(20 + scores[i + 2][2][0])
            elif scores[i + 1][1] == 'spare':
                updated_scores.append(10 + sum(scores[i + 1][2]))
            elif scores[i + 1][1] == 'regular':
                updated_scores.append(10 + sum(scores[i + 1][2]))
        elif score[1] == 'spare':
            updated_scores.append(score[0] + scores[i + 1][2][0])
        elif score[1] == 'regular':
            updated_scores.append(score[0])
        print(f"updated_scores: {updated_scores}\n{'*' * 50}")
    print(f"length updated_scores: {len(updated_scores)} ::: updated_scores: {updated_scores}")
    print(scores[:-1])
    return sum(updated_scores[:-1]) + sum(updated_scores[-1][-1])


a = bowling_score('11 11 11 11 11 11 11 11 11 11')  # , 20)
print('*' * 50)
b = bowling_score('X X X X X X X X X XXX')  # , 300)
print('*' * 50)
# c = bowling_score('X X 9/ 80 X X 90 8/ 7/ 44')
print('*' * 50)
d = bowling_score('X X 9/ 80 X X 90 8/ 7/ 44/')  # , 0)

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
