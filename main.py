from src.indexer import Indexer
from src.chatter import Chatter
import time


def main(openai_api_key, index_urls, to_store=False):
    indexer = Indexer(openai_api_key=openai_api_key)
    if to_store:
        index = indexer.create(index_urls=index_urls)
    index = indexer.load()

    chatter = Chatter(openai_api_key=openai_api_key)
    chatter.create_engine(index)


    prompt = ""

    while prompt != "q":
        if prompt == "":
            print("\n\nInput any prompt as you want!")
        prompt = input()
        if prompt == "":
            # print("Empty prompt is invalid. Try again!")
            continue
        elif prompt == "q":
            print(chatter.answer("Good bye! Have a nice day!"))
            break
        start = time.perf_counter()
        answer = chatter.answer(prompt)
        end = time.perf_counter()
        print("======= took {} s =============".format(str(end - start)))
        print(answer)



if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Simple OpenAI Chatbot sample")
    parser.add_argument("--config", help="configuration file", default="config/config.yaml")
    parser.add_argument("--store", help="To store index", default=False)

    args = parser.parse_args()

    config_file = args.config

    # print(args.store)

    import yaml
    with open(config_file, "r") as yml:
        config = yaml.safe_load(yml)

    main(config["openai_api_key"], config["index_urls"], args.store)
