import requests

BASE = "http://127.0.0.1:5000/"
test_req = {"normal":1, "dry":1, "oily":1, "combination":1, "acne":1, "sensitive":0, "fine lines":0, "wrinkles":0, "redness":1, "dull":0, "pore":0, "pigmentation":0, "blackheads":1, "whiteheads":0, "blemishes":1, "dark circles":0, "eye bags":1, "dark spots":0}

response = requests.put(BASE + "/recommend", test_req)
print(response.json())






# ("normal", type=int, help="Name of the video is required", required=True)
# rec_args.add_argument("dry", type=int, help="Name of the video is required", required=True)
# rec_args.add_argument("oily", type=int, help="Name of the video is required", required=True)

# rec_args.add_argument("combination", type=int, help="Name of the video is required", required=True)
# rec_args.add_argument("acne", type=int, help="Name of the video is required", required=True)
# rec_args.add_argument("sensitive", type=int, help="Name of the video is required", required=True)

# rec_args.add_argument("fine lines", type=int, help="Name of the video is required", required=True)
# rec_args.add_argument("wrinkles", type=int, help="Name of the video is required", required=True)
# rec_args.add_argument("redness", type=int, help="Name of the video is required", required=True)

# rec_args.add_argument("dull", type=int, help="Name of the video is required", required=True)
# rec_args.add_argument("pore", type=int, help="Name of the video is required", required=True)
# rec_args.add_argument("pigmentation", type=int, help="Name of the video is required", required=True)

# rec_args.add_argument("blackheads", type=int, help="Name of the video is required", required=True)
# rec_args.add_argument("whiteheads", type=int, help="Name of the video is required", required=True)
# rec_args.add_argument("blemishes", type=int, help="Name of the video is required", required=True)

# rec_args.add_argument("dark circles", type=int, help="Name of the video is required", required=True)
# rec_args.add_argument("eye bags", type=int, help="Name of the video is required", required=True)
# rec_args.add_argument("dark spots", type=int, help="Name of the video is required", required=True)