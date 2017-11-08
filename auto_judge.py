#!/usr/bin/python
import os
import zipfile
import rarfile
import shutil
import re
import patoolib
import subprocess

VERSION = 0.5
current_path = os.getcwd()
END_NAME = '/提交作业的附件/'


def check_folder(student_name):
    FORBIDDEN = ('DS_Store', 'py', 'code', 'judge', ".md", "git", ".idea")
    NECESSARY = ('.java')
    for item in FORBIDDEN:
        if item in student_name:
            return False
    return True


def find_compressed_file(student_names, zip_files):
    for student_name in student_names:
        if not check_folder(student_name):
            continue

        zip_file_folder = current_path + '/' + student_name + END_NAME
        compress_file_name = list(
            filter(lambda x: "zip" in x or 'rar' in x or '7z' in x, (os.listdir(zip_file_folder))))
        if compress_file_name != []:
            compress_file_name = compress_file_name[0]
            zip_files[student_name] = (zip_file_folder + compress_file_name)


def add_path(file_path, zip_path, names, name):
    #	number = re.compile("[0-9]+")
    keyword = re.compile("\.java")
    if re.search(keyword, names) != None:
        added_name = (zip_path + names)  # .replace(' ', '\ ')
        print(added_name)
        if name in file_path.keys():
            file_path[name].append(added_name)
        else:
            file_path[name] = [added_name]


def unzip_compressed_files(zip_files, file_path):
    for name, zip_path in zip_files.items():
        if 'zip' in zip_path:
            zip_file = zipfile.ZipFile(zip_path)
        elif 'rar' in zip_path:
            zip_file = rarfile.RarFile(zip_path)
        else:
            #			print(zip_path)
            #			quit()
            current_path = (zip_path[:zip_path.find(name)] + name + '/') + 'code/'
            if not os.path.isdir(current_path):
                os.mkdir(current_path)
            else:
                print(current_path)
                os.system('rm -f -r \'{}\''.format(current_path))
            patoolib.extract_archive(zip_path, outdir=current_path)
            New = True
            while New:
                files_in_dir = os.listdir(current_path)
                for item in files_in_dir:
                    New = False
                    if os.path.isdir(current_path + item):
                        current_path += item + '/'
                        New = True
                    else:
                        add_path(file_path, current_path, item, name)
            continue

        if not os.path.isdir("./" + name + '/'):
            os.mkdir("./" + name + '/')
        for names in zip_file.namelist():
            zip_file.extract(names, "./" + name + '/')
            add_path(file_path, zip_path[:zip_path.rfind('/') + 1], names, name)
        zip_file.close()

    ## print loaded info
    print('Loaded {} students'.format(len(file_path.keys())))
    for key in (file_path.keys()):
        print(key)


def compile_file(paths, file_info, package_pattern, class_name_pattern):
    print("reformating...")
    error = ""
    for path in paths:
        # compile
        real_path = path.replace('/提交作业的附件', "")
        print("\t", real_path)
        with open(real_path, 'rb') as f:
            try:
                content = (f.read().decode('gbk'))
            except UnicodeDecodeError:
                content = (f.read().decode('utf-8'))
        content = (re.sub(package_pattern, "", content))
        try:
            class_name = re.findall(class_name_pattern, content)[0]
        except IndexError:
            error += real_path + '\n'
            print('\terror: cannot found class name of .java file', real_path + real_path[real_path.rfind('/'):])
            

        with open('./{}.java'.format(class_name), 'w') as f:
            # print("content:", content)
            f.write(content.encode('utf-8').decode('utf-8'))

        file_info[class_name] = real_path
    return error

def run_file(file_info, select_dict, student_name):
    # run
    print('testing...')
    error = ""
    for class_name, real_path in file_info.items():
        print("\t", class_name)
        result, err = pipe('javac ./{}.java'.format(class_name))
        if err != b"":
            error += "runtime error: {}\n".format(real_path) 
        test_file = select_test_file(class_name, select_dict)
        if not test_file:
            error += real_path + '\n'
            print('\terror: cannot find a match test file in ./judge/judge.profile',
                  real_path + real_path[real_path.rfind('/'):])
            continue
        for single_test_file in test_file.split(' '):
            if single_test_file != '' and single_test_file != None:
                (out, err) = pipe('java {} < ./{}'.format(class_name, single_test_file))
                if (err!= b""):
                    error += " compile error:" + real_path + '\n'
                else:
                    result = out.decode("utf-8")
                    if student_name in judge_dict.keys():
                    	judge_dict[student_name] += test_file + '\t: ' + result + '\n'
                    else:
                    	judge_dict[student_name] = test_file + '\t: ' + result + '\n'

    return error
    
def pipe(command):
    proc = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True, stderr = subprocess.PIPE)
    return proc.communicate()

def judge_file(file_path, judge_dict, select_dict):
    error = ''
    package_pattern = re.compile("package.*?;")
    class_name_pattern = re.compile("public class ([a-zA-Z0-9_]+)[ \t{]*")
    os.chdir('./judge')
    for name, paths in file_path.items():
        print('judging', name)
        file_info = {}
        compile_file(paths, file_info, package_pattern, class_name_pattern)
        error += run_file(file_info, select_dict, name)
    return error


def select_test_file(path, select_dict):
    pattern = re.compile("11[0-9]+")
    path = re.sub(pattern, "", path)
    for key in select_dict.keys():
        if key.upper() in path.upper():
            return select_dict[key]


def give_result(judge_dict, error_file):
    content = ''
    for key, value in judge_dict.items():
        content += '#' + key + '\n'
        content += value + '\n'
    with open('./result.md', 'w') as f:
        f.write(content)
    with open('./error.md', 'w') as f:
        f.write(error_file)
    os.system('rm -f *.class *.java *.result')


def check_judge_files():
    if not os.path.isdir('./judge'):
        print('You have not creted judge folder yet!')
        p_quit(False)
    if not os.path.isfile("./judge/judge.profile"):
        print('You have not creted judge.profile in ./judge yet!')
        p_quit(False)


def load_judge_profile(select_dict):
    check_judge_files()

    with open('./judge/judge.profile', 'r') as f:
        content = f.read()
    lines = content.split('\n')

    for line in lines:
        if line == "" or line == None:
            continue
        keys, values = line.split(":")
        values = values.strip()
        for key in keys.split(' '):
            if key == "":
                continue
            if key == 'IGNORE':
                select_dict['IGNORE'] = values.split(' ')
                continue
            if key not in select_dict.keys():
                select_dict[key] = values
            else:
                select_dict[key] += (values)

    check_test_file(select_dict)


def check_test_file(select_dict):
    patterns = r''
    if 'IGNORE' in select_dict.keys():
        ignore_items = select_dict['IGNORE']
        patterns = [re.compile(item) for item in ignore_items]
    for key, values in select_dict.items():
        if key == "IGNORE":
            continue
        for value in values.split(" "):
            for pattern in patterns:
                value = re.sub(pattern, "", value)
            print(value)
            if value == "" and value == None:
                continue
            if not os.path.isfile('./judge/' + value):
                print('the {} test file is not in ./judge'.format(value))
                p_quit(False)


def p_quit(success):
    if success:
        success_print()
    else:
        failiure_print()
    print("--------------------------------------")
    print("Programmed by Boris, 11510237@mail.sustc.edu.cn")
    print("Ver. {}".format(VERSION))
    quit()


def failiure_print():
    pass


def success_print():
    print("--------------------------------------")
    print("The auto-judge has finished.")
    print("You may check the result.md and error.md in ./judge")


if __name__ == "__main__":
    student_names = filter(lambda x: not "py" in x, os.listdir(current_path))
    zip_files = {}
    file_path = {}
    judge_dict = {}
    select_dict = {}
    load_judge_profile(select_dict)
    find_compressed_file(student_names, zip_files)
    unzip_compressed_files(zip_files, file_path)
    error = judge_file(file_path, judge_dict, select_dict)
    give_result(judge_dict, error)
    p_quit(True)
