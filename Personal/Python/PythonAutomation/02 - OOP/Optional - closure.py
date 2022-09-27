""" Exemplu de implementare a nested functions  - Monitorizarea unui threshold"""

import psutil  # utitar care ne permite sa avem un view catre partea de performance testing



def get_memory():
    """get the current free memory"""
    return psutil.virtual_memory().percent


memory = get_memory()
print(memory)


def memory_logger(msg):
    """Log memory data for checking"""
    def logger():
        print(f"Logging memory data {msg}.")

        def another_logger():
            print("Just checking nested functions")

        another_logger()

    logger()


memory_logger(memory)


# -----------------------------------------------------

def closure_memory_logger(msg):
    """define the threshold and print message"""
    threshold = 90
    def logger():
        print(f"Logging memory data with closure {msg}, keep an eye to the threshold {threshold}")
    return logger


print("----------------------------")

# cl = closure_memory_logger(memory)
closure_memory_logger(memory)()
# print(cl)
# cl()
