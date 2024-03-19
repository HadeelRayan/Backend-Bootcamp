import random
failure_probability = 0 # Initial failure probability


def raise_random_exception_with_probability():
    global failure_probability
    try:
        if random.random() < failure_probability:
            # Raise a random exception
            random_exception = random.choice([
                FileNotFoundError,
                PermissionError,
                IsADirectoryError,
                FileExistsError,
                NotADirectoryError,
                IOError
            ])
            raise random_exception("Random exception raised")
        else:
            ### READ/WRITE CODE HERE ###
            if failure_probability < 1.0: # Cap the failure probability at 100%
                failure_probability += 0.05 # Increase failure probability

    except Exception as e:
        failure_probability = 0 # Reset failure probability upon failure
        raise e
