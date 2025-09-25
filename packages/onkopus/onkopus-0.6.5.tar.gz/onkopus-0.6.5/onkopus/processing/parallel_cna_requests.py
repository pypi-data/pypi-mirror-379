import copy, gzip, os, traceback, time
from multiprocessing import Process, Pool
import copy
import adagenes
import onkopus as op
from threading import Thread
from onkopus.processing.threads import ThreadWithReturnValue

def parallel_requests1(annotated_data, genome_version="hg38",oncokb_key=None):
    """
    Annotates a biomarker frame with parallelized Onkopus requests

    :param annotated_data:
    :param genome_version:
    :param oncokb_key: Private OncoKB account access token (Required for including OncoKB results)
    :return:
    """
    start_time = time.time()

    task1 = op.ProteinDomainCNAClient(genome_version=genome_version).process_data
    task2 = op.DGIdbClient(genome_version=genome_version).process_data
    #task2 = onkopus.onkopus_clients.CIViCGeneClient(genome_version=genome_version).process_data

    # pathogenicity

    # transcripts

    # protein IDs

    # molecular and protein features

    # drug gene interactions

    # gene expression

    # Breakpoint analysis

    annotated_data_oncokb = copy.deepcopy(annotated_data)
    annotated_data_oncokb["oncokbkey"] = oncokb_key

    t1 = ThreadWithReturnValue(target=task1, args=[annotated_data])
    t2 = ThreadWithReturnValue(target=task2, args=[annotated_data])

    t1.start()
    t2.start()

    data1 = t1.join()
    data2 = t2.join()

    annotated_data = adagenes.merge_dictionaries(annotated_data, data1)
    annotated_data = adagenes.merge_dictionaries(annotated_data, data2)

    stop_time = time.time() - start_time
    print("Time for parallel annotation requests: ",stop_time)

    return annotated_data


def parallel_requests(annotated_data, genome_version="hg38",oncokb_key=None):
    """
    Annotates a biomarker frame with parallelized Onkopus requests

    :param annotated_data:
    :param genome_version:
    :param oncokb_key: Private OncoKB account access token (Required for including OncoKB results)
    :return:
    """
    start_time = time.time()

    task1 = op.GENCODECNAClient(genome_version=genome_version).process_data
    task2 = op.CNASphereGenesClient(genome_version=genome_version).process_data
    task3 = op.CNVoyantClient(genome_version=genome_version).process_data
    task4 = op.ClassifyCNVClient(genome_version=genome_version).process_data
    task5 = op.XCNVClient(genome_version=genome_version).process_data
    task6 = op.ISVClient(genome_version=genome_version).process_data
    task7 = op.TADAClient(genome_version=genome_version).process_data
    task8 = op.DBCNVClient(genome_version=genome_version).process_data

    t1 = ThreadWithReturnValue(target=task1, args=[annotated_data])
    t2 = ThreadWithReturnValue(target=task2, args=[annotated_data])
    t3 = ThreadWithReturnValue(target=task3, args=[annotated_data])
    #t4 = ThreadWithReturnValue(target=task4, args=[annotated_data,True])
    t4 = ThreadWithReturnValue(target=task4, args=[annotated_data])
    t5 = ThreadWithReturnValue(target=task5, args=[annotated_data])
    t6 = ThreadWithReturnValue(target=task6, args=[annotated_data])
    t7 = ThreadWithReturnValue(target=task7, args=[annotated_data])
    t8 = ThreadWithReturnValue(target=task8, args=[annotated_data])

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()

    data1 = t1.join()
    data2 = t2.join()
    data3 = t3.join()
    data4 = t4.join()
    data5 = t5.join()
    data6 = t6.join()
    data7 = t7.join()
    data8 = t8.join()

    annotated_data = adagenes.merge_dictionaries(annotated_data, data1)
    annotated_data = adagenes.merge_dictionaries(annotated_data, data2)
    annotated_data = adagenes.merge_dictionaries(annotated_data, data3)
    annotated_data = adagenes.merge_dictionaries(annotated_data, data4)
    annotated_data = adagenes.merge_dictionaries(annotated_data, data5)
    annotated_data = adagenes.merge_dictionaries(annotated_data, data6)
    annotated_data = adagenes.merge_dictionaries(annotated_data, data7)
    annotated_data = adagenes.merge_dictionaries(annotated_data, data8)

    stop_time = time.time() - start_time
    print("Time for parallel annotation requests: ",stop_time)

    return annotated_data

