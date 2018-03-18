
import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

if __name__ == "__main__":
    
    sc = SparkContext(appName= "StreamingData")
    ssc = StreamingContext(sc, 2)
    
    ssc.checkpoint(os.path.join(os.path.pardir, "real-time-streaming", 'tmp'))
    
    lines = ssc.socketTextStream("localhost", 7777)
    
    def count_words(newValues, lastSum):
        if lastSum is None:
            lastSum = 0
        return sum(newValues, lastSum)
    
    words_counts = lines.flatMap(lambda line: line.split(" "))\
                    .filter(lambda word: "ERROR" in word)\
                    .map(lambda word: (word, 1))\
                    .updateStateByKey(countwords)
    
    words_counts.pprint()
    
    ssc.start()
    ssc.awaitTermination()