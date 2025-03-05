from meshroom.decorators import setup_producer


@setup_producer("carots", order="first")
def setup_soar_producer_for_carots():
    print("I have setup the producer mySOAR-side for carots")
