import subprocess

def checout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False

def hash_crc(cmd):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if result.returncode == 0:
        return result

path_in = '/home/user/tst'
path_out = '/home/user/out'
path_ext = '/home/user/folder1'
path_ext2 = '/home/user/folder2'

#test_1
def test_step1():
    res_1 = checout(f'cd {path_in}; 7z a ../out/arx2', 'Everything is Ok')
    res_2 = checout(f'ls {path_out}', 'arx2.7z')
    assert res_1 and res_2, print('test_1 FAIL')

#test_2
def test_step2():
    res_1 = checout(f"cd {path_out}; 7z e arx2.7z -o{path_ext} -y", "Everything is Ok"), print('test_2 FAIL')
    res_2 = checout(f"ls {path_ext}", 'text_1.txt'), print('test_2 FAIL')
    assert res_1 and res_2, print('test_2 FAIL')
#test_3
def test_step3():
    assert checout(f'cd {path_out}; 7z t arx2.7z', 'Everything is Ok'), print('test_1 FAIL')
#test_4
def test_step4():
    assert checout(f'cd {path_out}; 7z u arx2.7z', 'Everything is Ok'), print('test_4 FAIL')

#test_5
def test_step5():
    res_1 = checout(f'cd {path_ext}; 7z l arx2.7z', 'arx2.7z')
    res_2 = checout(f'cd {path_ext}; 7z l arx2.7z', 'stepwise')
    assert res_1 and res_2, print('test_5 FAIL')

#test_6
def test_step6():
    res_1 = checout(f"cd {path_in}; 7z x arx2.7z -o {path_ext2} -y", "Everything is Ok"), print('test_6 FAIL')
    res_2 = checout(f"ls {path_ext2}", 'test_1'), print('test_2 FAIL')
    assert res_1 and res_2, print('test_2 FAIL')

#test_7
def test_step7():
    checout(f'cd {path_out}; 7z d arx2.7z', 'Everything is Ok'), print('test_7 FAIL')


#test_8
def test_step8():
    res_1 = checout(f"cd {path_ext}; 7z h text_1.txt", "Everything is Ok"), print('test_8 FAIL')
    hash_ = hash_crc(f"cd {path_ext}; crc32 text_1.txt")
    res_2 = checout(f"cd {path_ext}; 7z h text_1.txt", 'hash'), print('test_8 FAIL')
    assert res_1 and res_2, print('test_2 FAIL')

