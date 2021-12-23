from mailcap import show

import pandas as pd
import numpy as np

# df_listly = pd.read_csv('D:/LiST/Vanple/Vanple/LISTLY_TRIAL_20210726_5G.xlsx')
# df_vanple = pd.read_csv('D:/LiST/Vanple/Vanple/밴플_차박지도.xlsx')

df_listly = pd.read_excel('D:/LiST/Vanple/Vanple/LISTLY_TRIAL_20210726_5G.xlsx')
df_vanple = pd.read_excel('D:/List/Vanple/Vanple/밴플_차박지도.xlsx')
df_vanple = df_vanple.drop(index = 0)
df_vanple = df_vanple.reset_index()

# Null값으로 두고 POI명 수정
df_listly['이름'] = df_listly['이름'].str.replace('야영금지', '')
df_listly['이름'] = df_listly['이름'].str.replace('진입불가', '')
df_listly['이름'] = df_listly['이름'].str.replace('폐쇄', '')
df_listly['이름'] = df_listly['이름'].str.replace('    ', '')


df_listly.to_excel('D:/LiST/Vanple/Vanple/5GCAMP.xlsx', index=False)

# for x in range(0, df_listly.shape[0]):
    # if df_listly['이름'][x] == '야영금지':
    #     df_listly = df_listly['이름'][x].str.replace('야영금지', '')
    #     df_listly = df_listly['이름'][x].str.replace('    ', '')
    # elif df_listly['이름'][x] == '진입불가':
    #     df_listly = df_listly['이름'][x].str.replace('진입불가', '')
    #     df_listly = df_listly['이름'][x].str.replace('    ', '')
    # elif df_listly['이름'][x] == '폐쇄':
    #     df_listly = df_listly['이름'][x].str.replace('폐쇄', '')
    #     df_listly = df_listly['이름'][x].str.replace('    ', '')



# 가능 유무 처리
# for x in range(0, df_listly.shape[0]):
#     if df_listly['주변 공중화장실'][x] == '주변 공중 화장실':
#         df_listly['주변 공중화장실'][x] = '사용가능'
#     else:
#         df_listly['주변 공중화장실'][x] = '사용불가'
# for y in range(0, df_listly.shape[0]):
#     if df_listly['주변 개수대'][y] == '주변 개수대':
#         df_listly['주변 개수대'][y] = '사용가능'
#     else:
#         df_listly['주변 개수대'][y] = '사용불가'
# for z in range(0, df_listly.shape[0]):
#     if df_listly['주변 수돗물'][z] == '주변 수돗물 사용 가능':
#         df_listly['주변 수돗물'][z] = '사용가능'
#     else:
#         df_listly['주변 수돗물'][z] = '사용불가'
#
# for a in range(0, df_listly.shape[0]):
#     if df_listly['승용차 진입'][a] == '승용차 진입 가능':
#         df_listly['승용차 진입'][a] = '진입가능'
#     else:
#         df_listly['승용차 진입'][a] = '진입불가'
#
# for b in range(0, df_listly.shape[0]):
#     if df_listly['SUV차량만 진입'][b] == 'SUV차량만 진입가능':
#         df_listly['SUV차량만 진입'][b] = '진입가능'
#     else:
#         df_listly['SUV차량만 진입'][b] = '진입불가'
#
# for c in range(0, df_listly.shape[0]):
#     if df_listly['소형 트레일러 접근'][c] == '소형 트레일러 접근 가능':
#         df_listly['소형 트레일러 접근'][c] = '접근가능'
#     else:
#         df_listly['소형 트레일러 접근'][c] = '접근불가'
#
#
# for d in range(0, df_listly.shape[0]):
#     if df_listly['카라반 접근'][d] == '카라반 접근 가능':
#         df_listly['카라반 접근'][d] = '접근가능'
#     else:
#         df_listly['카라반 접근'][d] = '접근불가'
#
# for e in range(0, df_listly.shape[0]):
#     if df_listly['루프탑 접근'][e] == '루프탑 접근 가능':
#         df_listly['루프탑 접근'][e] = '접근가능'
#     else:
#         df_listly['루프탑 접근'][e] = '접근불가'
#
# for f in range(0, df_listly.shape[0]):
#     if df_listly['캠핑카 접근'][f] == '캠핑카 접근 가능':
#         df_listly['캠핑카 접근'][f] = '접근가능'
#     else:
#         df_listly['캠핑카 접근'][f] = '접근불가'
#
# for g in range(0, df_listly.shape[0]):
#     if df_listly['도보로만 접근'][g] == '도보로만 접근 가능':
#         df_listly['도보로만 접근'][g] = '접근가능'
#     else:
#         df_listly['도보로만 접근'][g] = '접근불가'
#
# for h in range(0, df_listly.shape[0]):
#     if df_listly['등산'][h] == '등산':
#         df_listly['등산'][h] = '등산지역 있음'
#     else:
#         df_listly['등산'][h] = '등산지역 없음'
# for i in range(0, df_listly.shape[0]):
#     if df_listly['체육시설'][i] == '체육시설':
#         df_listly['체육시설'][i] = '체육시설 있음'
#     else:
#         df_listly['체육시설'][i] = '체육시설 없음'
# for j in range(0, df_listly.shape[0]):
#     if df_listly['박물관'][j] == '박물관':
#         df_listly['박물관'][j] = '박물관 있음'
#     else:
#         df_listly['박물관'][j] = '박물관 없음'
# for k in range(0, df_listly.shape[0]):
#     if df_listly['미술관/갤러리'][k] == '미술관/갤러리':
#         df_listly['미술관/갤러리'][k] = '미술관/갤러리 있음'
#     else:
#         df_listly['미술관/갤러리'][k] = '미술관/갤러리 없음'
# for l in range(0, df_listly.shape[0]):
#     if df_listly['무대/공연장'][l] == '무대/공연장':
#         df_listly['무대/공연장'][l] = '무대/공연장 있음'
#     else:
#         df_listly['무대/공연장'][l] = '무대/공연장 없음'
# for m in range(0, df_listly.shape[0]):
#     if df_listly['수영장'][m] == '수영장':
#         df_listly['수영장'][m] = '수영장 있음'
#     else:
#         df_listly['수영장'][m] = '수영장 없음'
# for n in range(0, df_listly.shape[0]):
#     if df_listly['생태공원'][n] == '생태공원':
#         df_listly['생태공원'][n] = '생태공원 있음'
#     else:
#         df_listly['생태공원'][n] = '생태공원 없음'
# for o in range(0, df_listly.shape[0]):
#     if df_listly['잔디광장'][o] == '잔디광장':
#         df_listly['잔디광장'][o] = '잔디광장 있음'
#     else:
#         df_listly['잔디광장'][o] = '잔디광장 없음'
#
# for p in range(0, df_listly.shape[0]):
#     if df_listly['수상 레저'][p] == '수상 레저':
#         df_listly['수상 레저'][p] = '수상 레저 있음'
#     else:
#         df_listly['수상 레저'][p] = '수상 레저 없음'
#
# for q in range(0, df_listly.shape[0]):
#     if df_listly['주변 샤워시설'][q] == '주변 샤워시설':
#         df_listly['주변 샤워시설'][q] = '샤워시설 있음'
#     else:
#         df_listly['주변 샤워시설'][q] = '샤월시설 없음'
#
# for r in range(0, df_listly.shape[0]):
#     if df_listly['주변 전기'][r] == '주변 전기 이용 가능':
#         df_listly['주변 전기'][r] = '이용가능'
#     else:
#         df_listly['주변 전기'][r] = '이용불가'
#
# for s in range(0, df_listly.shape[0]):
#     if df_listly['물놀이'][s] == '물놀이':
#         df_listly['물놀이'][s] = '물놀이 가능'
#     else:
#         df_listly['물놀이'][s] = '물놀이 불가'
#
# for t in range(0, df_listly.shape[0]):
#     if df_listly['민물낚시'][t] == '민물낚시':
#         df_listly['민물낚시'][t] = '민물낚시 가능'
#     else:
#         df_listly['민물낚시'][t] = '민물낚시 불가'
#
# for u in range(0, df_listly.shape[0]):
#     if df_listly['바다낚시'][u] == '바다낚시':
#         df_listly['바다낚시'][u] = '바다낚시 가능'
#     else:
#         df_listly['바다낚시'][u] = '바다낚시 불가'
#
# state_list = list()
# for w in range(0, df_listly.shape[0]):
#     df_listly['이름'][w].rstrip(' ')
#     if df_listly['이름'][w] == '야영금지':
#         df_listly['이름'][w] = df_listly['이름'][w].replace('야영금지', '')
#         state_list.append('야영금지')
#     elif df_listly['이름'][w] == '진입불가':
#         df_listly['이름'][w] = df_listly['이름'][w].replace('진입불가', '')
#         state_list.append('진입불가')
#     else:
#         state_list.append('차박가능')
#     df_listly['이름'][w].lstrip(' ')
#
#
# nm_list = list()
# for x in range(0, df_listly.shape[0]):
#     nm_list += df_listly['이름'][x]
#
# for y in nm_list:
#     if nm_list[y] == '야영금지':
#         nm_list[y] = nm_list[y].replace('야영금지', '')
#
# df_listly['상태'] = state_list
#
# df_listly.to_excel('D:/LiST/Vanple/Vanple/LISTLY.xlsx')
# df_pListly = pd.read_excel('D:/LiST/Vanple/Vanple/LISTLY.xlsx')
#
# df_merge = pd.merge(df_vanple, df_pListly, how = 'left', on = '주소')
#
#
# df_merge.to_excel('D:/LiST/Vanple/Vanple/df_merge.xlsx')
#
# df_merge_org = pd.read_excel('D:/LiST/Vanple/Vanple/df_merge.xlsx')
# df_ex = pd.DataFrame
# col = df_merge_org.columns
#
# mask = df_merge_org['이름_x'] != df_merge_org['이름_y']
# df_filter = df_merge_org.loc[mask, :]
#
# df_filter.to_excel('D:/LiST/Vanple/Vanple/df_filter.xlsx')






# for v in range(0, df_merge_org.shape[0]):
#     if df_merge_org['이름_x'][v] == df_merge_org['이름_y'][v]:
#         df_merge_org.drop(df_merge_org.iloc[v:v+1, :])
# df_ex.set_index('이름_y', inplace=True)















# print(df_pListly.shape[0])
# print(df_vanple.shape[0])

# pL_va = df_pListly.shape[0] - df_vanple.shape[0]
# col = df_pListly.columns
# df_pre = pd.DataFrame()
#
#
# for v in range(0, df_pListly.shape[0]):
#     for w in range(0, df_vanple.shape[0]):
#         if df_pListly['주소'][v] == df_vanple['주소'][w] and df_pListly['이름'][v] != df_vanple['이름'][w]:
#             df_pre.append(df_pListly.iloc[v:v+1, :])
#             continue
#         else:
#             pass
#
# print(df_pre)






# x = 8
# for j in range(x, 12):
#     for i in range(0, 353):
#         try:
#             print(df_listly[i])
#         except KeyError:
#             print('what?')




# x = 8
# for j in range(x, 12):
#     for i in range(0, df_listly.shape[0]):
#         if df_listly.ix[i,x] == '주변 화장실 없음' or df_listly.ix[i,x] == '주변 개수대 없음' or df_listly.isnull() :
#             df_listly.ix[i, x] = '사용불가'
#
#         else:
#             df_listly[i][x] = '사용가능'



# df_merge.to_excel('D:/LiST/Vanple/Vanple/밴플_리스틀리_이너.xlsx')
# df_merge.to_excel('D:/LiST/Vanple/Vanple/밴플_리스틀리_왼쪽.xlsx')
# df_merge.to_excel('D:/LiST/Vanple/Vanple/밴플_리스틀리_주소_이름.xlsx')






# pd.merge(on='주소')