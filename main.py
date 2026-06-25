# Bayes Weather AI Classifier


def get_yes_or_no_input(question):
    """
    Ask the user a yes/no question and return True for yes and False for no.
    """

    while True:
        answer = input(question + " (yes/no): ").lower().strip()

        if answer == "yes":
            return True
        elif answer == "no":
            return False
        else:
            print("Please type yes or no.")


def calculate_winter_probability(is_cold, is_rainy, is_windy):
    """
    Calculate the probability that it is winter based on weather evidence.

    This uses a simple Naive Bayes approach.

    Bayes idea:
    P(Winter | Evidence) = P(Evidence | Winter) * P(Winter)

    We compare:
    - probability score for Winter
    - probability score for Not Winter

    Then we normalize the scores so they add up to 1.
    """

    # Prior probabilities
    p_winter = 0.30
    p_not_winter = 0.70

    # Likelihoods for winter
    # These are example values for learning purposes.
    p_cold_given_winter = 0.90
    p_rainy_given_winter = 0.60
    p_windy_given_winter = 0.50

    # Likelihoods for not winter
    p_cold_given_not_winter = 0.25
    p_rainy_given_not_winter = 0.30
    p_windy_given_not_winter = 0.40

    # Start each score with the prior probability
    winter_score = p_winter
    not_winter_score = p_not_winter

    # Update score based on cold evidence
    if is_cold:
        winter_score *= p_cold_given_winter
        not_winter_score *= p_cold_given_not_winter
    else:
        winter_score *= 1 - p_cold_given_winter
        not_winter_score *= 1 - p_cold_given_not_winter

    # Update score based on rainy evidence
    if is_rainy:
        winter_score *= p_rainy_given_winter
        not_winter_score *= p_rainy_given_not_winter
    else:
        winter_score *= 1 - p_rainy_given_winter
        not_winter_score *= 1 - p_rainy_given_not_winter

    # Update score based on windy evidence
    if is_windy:
        winter_score *= p_windy_given_winter
        not_winter_score *= p_windy_given_not_winter
    else:
        winter_score *= 1 - p_windy_given_winter
        not_winter_score *= 1 - p_windy_given_not_winter

    # Normalize the scores
    total_score = winter_score + not_winter_score

    probability_winter = winter_score / total_score
    probability_not_winter = not_winter_score / total_score

    return probability_winter, probability_not_winter


def explain_result(probability_winter, probability_not_winter):
    """
    Print the final result and explain the AI-style decision.
    """

    print("\nResults")
    print("-------")
    print(f"P(Winter | Evidence): {probability_winter:.2f}")
    print(f"P(Not Winter | Evidence): {probability_not_winter:.2f}")

    if probability_winter > probability_not_winter:
        print("\nPrediction: Winter is likely.")
    else:
        print("\nPrediction: Winter is not likely.")

    print("\nExplanation")
    print("-----------")
    print("The program starts with a prior probability of winter.")
    print("It then updates that probability using evidence such as cold, rainy, and windy weather.")
    print("This is an example of a simple AI classifier making a decision under uncertainty.")


def main():
    """
    Main program function.
    """

    print("Bayes Weather AI Classifier")
    print("---------------------------")
    print("This program predicts whether it is likely to be winter.")
    print("It uses Bayes' theorem and conditional probability.\n")

    # Get evidence from the user
    is_cold = get_yes_or_no_input("Is it cold?")
    is_rainy = get_yes_or_no_input("Is it rainy?")
    is_windy = get_yes_or_no_input("Is it windy?")

    # Calculate probabilities
    probability_winter, probability_not_winter = calculate_winter_probability(
        is_cold,
        is_rainy,
        is_windy
    )

    # Show result
    explain_result(probability_winter, probability_not_winter)


if __name__ == "__main__":
    main()
