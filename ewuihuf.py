import os

import random

import string

from tronpy import Tron

from tronpy.keys import PrivateKey
import time
def generate_tron_account():

    """

    生成一个 TRON 账户的私钥和地址。

    """

    # 生成随机私钥

    private_key = PrivateKey.random()

    # 获取对应的地址

    address = private_key.public_key.to_base58check_address()

    return private_key, address



def has_consecutive_chars(s, n=6):  # 将 n 从 6 改为 3

    """

    检查字符串 s 是否包含至少 n 个连续相同的字符。

    """

    if len(s) < n:

        return False

    for i in range(len(s) - n + 1):

        substring = s[i:i+n]

        if len(set(substring)) == 1:

            return True

    return False



def main(num_accounts=1000, output_file='tron_accounts_with_consecutive.txt'):
    


    """

    主函数，生成指定数量的 TRON 账户，并筛选出符合条件的账户。



    :param num_accounts: 要生成的账户数量

    :param output_file: 输出符合条件的账户信息的文件名

    """

    tron = Tron()

    matched_accounts = []



    print(f"正在生成 {num_accounts} 个 TRON 账户并筛选符合条件的账户...")



    for i in range(1, num_accounts + 1):

        private_key, address = generate_tron_account()

        

        if has_consecutive_chars(address, 6):  # 修改这里为 3

            matched_accounts.append((private_key, address))

            print(f"地址:{address},{private_key}")
        if i%10000000==0:
            print(f"创建了{i}个账户")



        



    print(f"生成完成！共找到 {len(matched_accounts)} 个符合条件的账户。")



    if matched_accounts:

        with open(output_file, 'w', encoding='utf-8') as f:

            for pk, addr in matched_accounts:

                f.write(f"地址: {addr}\n私钥: {pk}\n\n")

        print(f"符合条件的账户信息已保存到 {output_file}")

    else:

        print("未找到符合条件的账户。")



if __name__ == "__main__":
    

    # 设置要生成的账户数量

    num_accounts = 20000000  # 根据需要调整
        
        



    # 运行主函数

    main(num_accounts)
