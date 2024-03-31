with (open('1.txt', 'r', encoding='utf-8') as txt_1,
      open('2.txt', 'r', encoding='utf-8') as txt_2,
      open('3.txt', 'r', encoding='utf-8') as txt_3,
      open('completed_text_for_task_3.txt', 'w', encoding='utf-8') as completed_text):

    all_text_dict = ({'1.txt': txt_1.readlines(),
                     '2.txt': txt_2.readlines(),
                     '3.txt': txt_3.readlines()})

    sorting_str = dict(sorted(all_text_dict.items(), key=lambda item: item[1], reverse=True))

    for str_ in sorting_str.items():
        completed_text.write(f'{str_[0]}\n')
        completed_text.write(f'{len(str_[1])}\n')
        completed_text.write(f'\n')
        for line in str_[1]:
            if '\n' in line:
                completed_text.write(line)
            else:
                completed_text.write(f'{line}\n\n')