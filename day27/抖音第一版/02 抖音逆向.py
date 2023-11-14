import requests
import execjs
import os
import time

with open("01 源码.js") as f:
    js_code = f.read()

js_compile = execjs.compile(js_code)

user_id = "MS4wLjABAAAABAWrs5p4EI5wyeHaULkphv3FMf8mQ6th9dAIvwvyRfQ"
params = f'device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id={user_id}&max_cursor=0&locate_query=false&show_live_replay_strategy=1&need_time_list=1&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=en&browser_platform=Win32&browser_name=Chrome&browser_version=118.0.0.0&browser_online=true&engine_name=Blink&engine_version=118.0.0.0&os_name=Windows&os_version=10&cpu_core_num=12&device_memory=8&platform=PC&downlink=2.45&effective_type=4g&round_trip_time=150&webid=7300904390281610804&msToken=7-srHBUU5vMiv_tLWZ0al5OKftBReoNCxLK134G4zNHa_K6mP8P90NqCkM-uqFVysGTo-tshNqGcZT14Uk2-pA300cW6DirX5xuIiWJLMscnSai9T5o0N1xgz80='

xb = js_compile.call("window.jackson", params)
# print("xb:", xb)

url = "https://www.douyin.com/aweme/v1/web/aweme/post/?"
new_url = url + params + "&X-Bogus=" + xb

headers = {
    "Cookie": "ttwid=1%7CNM7EahTBTTv-y_td1JFLTasmRacsvkkdrSHMGX1g7-k%7C1699874282%7Ceb86c0a878ceb1d47a527e18b4de246fc442916730399353ec6cb7b311b263f8; douyin.com; device_web_cpu_core=12; device_web_memory_size=8; architecture=amd64; webcast_local_quality=null; home_can_add_dy_2_desktop=%220%22; passport_csrf_token=914504468915e6b8f95b8cfe725d1ad6; passport_csrf_token_default=914504468915e6b8f95b8cfe725d1ad6; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1700479084143%2C%22type%22%3A1%7D; strategyABtestKey=%221699874284.286%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.5%7D; s_v_web_id=verify_lowt9cbv_yGuk5Z5H_PHzx_4CKk_90bn_kIz3WOWqtOR5; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; csrf_session_id=1703398ba3435ef1d2e9e1cbefc6a2c0; ttcid=342a817fd0f6407980f8f33a16277c0537; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; SEARCH_RESULT_LIST_TYPE=%22single%22; download_guide=%223%2F20231113%2F0%22; __ac_nonce=065520d1d009993dc87c1; __ac_signature=_02B4Z6wo00f01BVpSMAAAIDByx8QZ99u-iQVSUxAAGAOz9TbCRvLV44Lz7Hz15cSnxDRpLi8rhp8EP5Lgt3aHqL.6JV6W1sIsYnLUho2xIMYO1ooaajJlVEb.MxtuP5pRKuBRl2nyqiPG3Wq39; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCS0dLdk5WVm5YcFoyN2RqdS9sN3k5Z2d0bjB5dmVadzNqVHI1MC9CQ1c2elBaZEtWOEVYeWJsZExhcHhSejBiTnJaSWw5cklHV0ZqbmZYTk5hWTMwb009IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; tt_scid=v0bkAkSUHQnhiPw5rAb.a7Hb.b0AY3GoAvlssnYyxR-QpoFkNotyibS9FzB6lXn9f5b6; msToken=NcuNC4M1T1wToosiOvl4fDKtB9UZynnrNkrQ1VNejRD424WLyUpPbomt0PGFxav0dvRffFoH2lXMvNDjH41mDkgt1r8Js-09-nlR57IUxAyObelIghdK4PV9boY=; msToken=7-srHBUU5vMiv_tLWZ0al5OKftBReoNCxLK134G4zNHa_K6mP8P90NqCkM-uqFVysGTo-tshNqGcZT14Uk2-pA300cW6DirX5xuIiWJLMscnSai9T5o0N1xgz80=; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1536%2C%5C%22screen_height%5C%22%3A864%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A12%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A2.45%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A150%7D%22; IsDouyinActive=true",
    "Referer": "https://www.douyin.com/user/MS4wLjABAAAASfM8dVUU44eRUmvB18pI_FBZIgyMBgmDYibYdyUiEV0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
}

res = requests.get(new_url, headers=headers)
# print("结果：", res.text)
author = res.json().get("aweme_list")[0].get("author").get("nickname")
root_path = author
if not os.path.exists(root_path):
    os.mkdir(root_path)

content_list = res.json().get("aweme_list")
for content in content_list:
    title = content.get("aweme_id")
    video_url = content.get("video").get("play_addr").get("url_list")[0]
    video_data = requests.get(url=video_url, headers=headers).content
    video_path = "./"+author+"/"+title+".mp4"
    with open(video_path, "wb") as fp:
        fp.write(video_data)
    print(title, video_url, ":保存下载成功！")
    cover_url = content.get("video").get("cover").get("url_list")[0]
    cover_data = requests.get(url=cover_url, headers=headers).content
    cover_path = "./" + author + "/" + title + ".jpg"
    with open(cover_path, "wb") as fp:
        fp.write(cover_data)
    print(title, cover_url, ":保存下载成功！")
    time.sleep(2)
