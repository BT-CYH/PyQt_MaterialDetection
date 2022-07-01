import os
import sys

def rename():
    output_path_all = "./svm/data/samples/All/"

    input_path = "./svm/data/samples/夹杂/"
    output_path = "./svm/data/samples/夹杂/"

    file_name = os.listdir(input_path)

    count = 1
    for file in file_name:
        os.rename(input_path+file, output_path+str(count)+"_jz.png")
        count += 1
    ####################################################
    input_path = "./svm/data/samples/裂纹/"
    output_path = "./svm/data/samples/裂纹/"
    file_name = os.listdir(input_path)

    count = 1
    for file in file_name:
        os.rename(input_path + file, output_path + str(count) + "_ck.png")
        count += 1

    ####################################################
    input_path = "./svm/data/samples/背景/"
    output_path = "./svm/data/samples/背景/"
    file_name = os.listdir(input_path)

    count = 1
    for file in file_name:
        os.rename(input_path + file, output_path + str(count) + "_bg.png")
        count += 1

    ####################################################
    input_path = "./svm/data/samples/夹杂/"
    file_name2 = os.listdir(input_path)
    for file in file_name2:
        os.rename(input_path + file, output_path_all + str(count) + "_jz.png")
        count += 1

    input_path = "./svm/data/samples/裂纹/"
    file_name2 = os.listdir(input_path)
    for file in file_name2:
        os.rename(input_path + file, output_path_all + str(count) + "_ck.png")
        count += 1

    input_path = "./svm/data/samples/背景/"
    file_name2 = os.listdir(input_path)
    for file in file_name2:
        os.rename(input_path + file, output_path_all + str(count) + "_bg.png")
        count += 1