# coding=utf-8
filename = 'metric_tags.txt'  # txt文件和当前脚本在同一目录下，所以不用写具体路径


def index1(filename):
    pos = []
    Efield = []
    with open(filename, 'r') as file_to_read:
        while True:
            lines = file_to_read.read()  # 整行读取数据
            if not lines:
                break
                pass
            # 将整行数据分割处理，如果分割符是空格，括号里就不用传入参数，如果是逗号， 则传入‘，'字符。
            p_tmp, E_tmp = [str(i) for i in lines.split()]
            pos.append(p_tmp)
            Efield.append(E_tmp)
            print p_tmp, E_tmp
            pass


def index2(filename):
    """
    read()的利弊：
    利：方便、简单；一次性独读出文件放在一个大字符串中，速度最快
    弊：文件过大的时候，占用内存会过大
    :param filename:
    :return:
    """
    file_object = open(filename)
    try:
        # file_context是一个string，读取完后，就失去了对test.txt的文件引用
        file_context = file_object.read()
        print 'file_context:\n', file_context
        # ile_context是一个list，每行文本内容是list中的一个元素
        file_context2 = file_object.read().splitlines()
        print 'file_context2:\n', file_context2
    finally:
        file_object.close()


def index3(filename):
    """
    readline()的利弊：
    利：占用内存小，逐行读取
    弊：由于是逐行读取，速度比较慢
    :param filename:
    :return:
    """
    with open(filename) as f:
        line = f.readline()
        while line:
            print line
            line = f.readline()


def index4(filename):
    """
    readlines()一次性读取文本的所有内容，结果是一个list
    这种方法读取的文本内容，每行文本末尾都会带一个'\n'换行符 (可以使用L.rstrip('\n')去掉换行符）
    readlines()的利端：
        一次性读取文本内容，速度比较快
    readlines()的弊端：
        随着文本的增大，占用内存会越来越多
    :param filename:
    :return:
    """
    with open(filename) as f:
        for line in f.readlines():
            print line


def index5(filename):
    file_object = open(filename, 'rU')
    try:
        for line in file_object:
            print line  # line带"\n"
    finally:
        file_object.close()


import mysql.connector

global conn, cursor


def readTxt(filename):
    """
    将.txt文件中的metric tags读取出
    :param filename:
    :return:
    """
    file_object = open(filename, 'rU')
    max_step = 3
    priority = 2
    func = 'all(#3)'
    op = '!='
    right_value = '1'
    tpl_id = 136
    run_begin = ''
    run_end = ''
    open_cursor()
    try:
        for line in file_object:
            # print line  # line带"\n"
            metric, tags = line.split()
            app_name = metric.split('.')[2]
            if metric.split('.')[3] == 'timing':
                continue
            app_point = tags.split('/')[2]
            note = '【' + app_name + '】' + app_point + '心跳(不等于1,且持续3分钟警告)'
            insert_row(metric, tags, max_step, priority, func, op, right_value, note,
                       run_begin, run_end, tpl_id)
            print metric, tags
    finally:
        file_object.close()
        close_cursor()


def open_cursor():
    global conn, cursor
    host, port, user, password, database = '10.70.14.215', 8080, 'root', '', 'falcon_portal'
    conn = mysql.connector.connect(host=host, port=port, user=user, password=password, database=database)
    cursor = conn.cursor()


def close_cursor():
    global conn, cursor
    conn.commit()
    cursor.close()


def insert_row(metric, tags, max_step, priority, func, op, right_value, note,
               run_begin, run_end, tpl_id):
    global cursor
    cursor.execute('insert into strategy (metric, tags, max_step, priority, func, op, '
                   'right_value, note,run_begin, run_end, tpl_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                   (metric, tags, max_step, priority, func, op, right_value, note, run_begin, run_end, tpl_id,))


if __name__ == '__main__':
    filename = 'metric_tags.txt'
    readTxt(filename)
