# #抓取 Medium.COM 的文章資料
# import urllib.request as req
# url="https://medium.com/_/api/home-feed"
# #建立一個 Request Header 和 Request data 的資訊
# request=req.Request(url,headers={
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
# })
# with req.urlopen(request) as response:
#     data=response.read().decode("utf-8") #根據觀察資料是 JSON 格式

# #解析 JSON 格式的資料，取得每篇文章的標題
# import json
# data=data.replace("])}while(1);</x>","") #因為資料不乾淨，把多餘的資料格式替換成空白
# data=json.load(data) #把原始的 JSON 資料解析成字典/列表的格式
# #取得 JSON 資料中的文章標題
# posts=data["payload"]["references"]["Post"]
# for key in posts:
#     post=posts[key]
#     print(post["title"])



#抓取 Medium.COM 的文章資料，加入Request Data的觀念(request payload/request body)
#F12 Network-XHR-preview找到標題的標籤，需一個一個找，找到post or title
#找到標題後從headers觀察連線資訊
#把request payload 原始碼全部複製一起發請求
import urllib.request as req
#建立連線網址
import json #因14行需發出data，為json的字典&utf-8格式，因此需做額外處理
url="https://medium.com/_/graphql"
#建立一個 Request Header 和 Request data 的資訊
requestData={"operationName":"ExtendedFeedQuery","variables":{"items":[{"postId":"397700e05ad2","topicId":""},{"postId":"755a02673aa9","topicId":""},{"postId":"11ce48a24fe3","topicId":""},{"postId":"68f75ca7cd6a","topicId":""},{"postId":"8641f20c482c","topicId":""},{"postId":"6079d407bbeb","topicId":""},{"postId":"a9f5f87f3118","topicId":""},{"postId":"79bbbbcf80b","topicId":""},{"postId":"d0618efc8944","topicId":""},{"postId":"3e66dfc4dfdf","topicId":""},{"postId":"8a4951564285","topicId":""},{"postId":"994bc437cb3d","topicId":""},{"postId":"7c0c5810bd4e","topicId":""},{"postId":"7499be1fc810","topicId":""},{"postId":"2bb35b658f7e","topicId":""},{"postId":"c1d36f2a213","topicId":""},{"postId":"35895ac9fe3a","topicId":""},{"postId":"8b633779ab8c","topicId":""},{"postId":"b0eb628e1de2","topicId":""},{"postId":"1ae3ec7959a4","topicId":""}]},"query":"query ExtendedFeedQuery($items: [ExtendedFeedItemOptions!]!) {\n  extendedFeedItems(items: $items) {\n    post {\n      ...PostListModulePostPreviewData\n      __typename\n    }\n    metadata {\n      topic {\n        id\n        name\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment PostListModulePostPreviewData on Post {\n  id\n  firstPublishedAt\n  readingTime\n  createdAt\n  mediumUrl\n  previewImage {\n    id\n    __typename\n  }\n  title\n  collection {\n    id\n    domain\n    slug\n    name\n    navItems {\n      url\n      __typename\n    }\n    logo {\n      id\n      __typename\n    }\n    avatar {\n      id\n      __typename\n    }\n    __typename\n  }\n  creator {\n    id\n    name\n    username\n    imageId\n    mediumMemberAt\n    ...userUrl_user\n    __typename\n  }\n  visibility\n  isProxyPost\n  isLocked\n  ...HomeFeedItem_post\n  ...HomeReadingListItem_post\n  ...HomeTrendingModule_post\n  __typename\n}\n\nfragment HomeFeedItem_post on Post {\n  __typename\n  id\n  title\n  firstPublishedAt\n  mediumUrl\n  collection {\n    id\n    name\n    domain\n    logo {\n      id\n      __typename\n    }\n    __typename\n  }\n  creator {\n    id\n    name\n    username\n    imageId\n    mediumMemberAt\n    __typename\n  }\n  previewImage {\n    id\n    __typename\n  }\n  previewContent {\n    subtitle\n    __typename\n  }\n  readingTime\n  tags {\n    ...TopicPill_tag\n    __typename\n  }\n  ...BookmarkButton_post\n  ...CreatorActionOverflowPopover_post\n  ...PostPresentationTracker_post\n  ...PostPreviewAvatar_post\n}\n\nfragment TopicPill_tag on Tag {\n  __typename\n  id\n  displayTitle\n}\n\nfragment BookmarkButton_post on Post {\n  ...SusiClickable_post\n  ...WithSetReadingList_post\n  ...AddToCatalogBookmarkButton_post\n  __typename\n  id\n}\n\nfragment SusiClickable_post on Post {\n  id\n  mediumUrl\n  ...SusiContainer_post\n  __typename\n}\n\nfragment SusiContainer_post on Post {\n  id\n  __typename\n}\n\nfragment WithSetReadingList_post on Post {\n  ...ReadingList_post\n  __typename\n  id\n}\n\nfragment ReadingList_post on Post {\n  __typename\n  id\n  viewerEdge {\n    id\n    readingList\n    __typename\n  }\n}\n\nfragment AddToCatalogBookmarkButton_post on Post {\n  ...AddToCatalogBase_post\n  __typename\n  id\n}\n\nfragment AddToCatalogBase_post on Post {\n  id\n  viewerEdge {\n    catalogsConnection {\n      catalogsContainingThis(type: LISTS) {\n        catalogId\n        catalogItemIds\n        __typename\n      }\n      predefinedContainingThis {\n        catalogId\n        predefined\n        catalogItemIds\n        __typename\n      }\n      __typename\n    }\n    ...editCatalogItemsMutation_postViewerEdge\n    ...useAddItemToPredefinedCatalog_postViewerEdge\n    __typename\n    id\n  }\n  ...WithToggleInsideCatalog_post\n  __typename\n}\n\nfragment useAddItemToPredefinedCatalog_postViewerEdge on PostViewerEdge {\n  id\n  catalogsConnection {\n    predefinedContainingThis {\n      catalogId\n      version\n      predefined\n      catalogItemIds\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment editCatalogItemsMutation_postViewerEdge on PostViewerEdge {\n  id\n  catalogsConnection {\n    catalogsContainingThis(type: LISTS) {\n      catalogId\n      version\n      catalogItemIds\n      __typename\n    }\n    predefinedContainingThis {\n      catalogId\n      predefined\n      version\n      catalogItemIds\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment WithToggleInsideCatalog_post on Post {\n  id\n  viewerEdge {\n    catalogsConnection {\n      catalogsContainingThis(type: LISTS) {\n        catalogId\n        __typename\n      }\n      predefinedContainingThis {\n        predefined\n        __typename\n      }\n      __typename\n    }\n    __typename\n    id\n  }\n  __typename\n}\n\nfragment CreatorActionOverflowPopover_post on Post {\n  allowResponses\n  id\n  statusForCollection\n  isLocked\n  isPublished\n  clapCount\n  mediumUrl\n  pinnedAt\n  pinnedByCreatorAt\n  curationEligibleAt\n  mediumUrl\n  responseDistribution\n  visibility\n  ...useIsPinnedInContext_post\n  pendingCollection {\n    id\n    name\n    creator {\n      id\n      __typename\n    }\n    avatar {\n      id\n      __typename\n    }\n    domain\n    slug\n    __typename\n  }\n  creator {\n    id\n    ...MutePopoverOptions_creator\n    ...auroraHooks_publisher\n    __typename\n  }\n  collection {\n    id\n    name\n    creator {\n      id\n      __typename\n    }\n    avatar {\n      id\n      __typename\n    }\n    domain\n    slug\n    ...MutePopoverOptions_collection\n    ...auroraHooks_publisher\n    __typename\n  }\n  ...ClapMutation_post\n  __typename\n}\n\nfragment MutePopoverOptions_creator on User {\n  id\n  __typename\n}\n\nfragment MutePopoverOptions_collection on Collection {\n  id\n  __typename\n}\n\nfragment ClapMutation_post on Post {\n  __typename\n  id\n  clapCount\n  ...MultiVoteCount_post\n}\n\nfragment MultiVoteCount_post on Post {\n  id\n  ...PostVotersNetwork_post\n  __typename\n}\n\nfragment PostVotersNetwork_post on Post {\n  id\n  voterCount\n  recommenders {\n    name\n    __typename\n  }\n  __typename\n}\n\nfragment useIsPinnedInContext_post on Post {\n  id\n  collection {\n    id\n    __typename\n  }\n  pendingCollection {\n    id\n    __typename\n  }\n  pinnedAt\n  pinnedByCreatorAt\n  __typename\n}\n\nfragment auroraHooks_publisher on Publisher {\n  __typename\n  ... on Collection {\n    isAuroraEligible\n    isAuroraVisible\n    viewerEdge {\n      id\n      isEditor\n      __typename\n    }\n    __typename\n    id\n  }\n  ... on User {\n    isAuroraVisible\n    __typename\n    id\n  }\n}\n\nfragment PostPresentationTracker_post on Post {\n  id\n  visibility\n  previewContent {\n    isFullContent\n    __typename\n  }\n  collection {\n    id\n    slug\n    __typename\n  }\n  __typename\n}\n\nfragment PostPreviewAvatar_post on Post {\n  __typename\n  id\n  collection {\n    id\n    name\n    ...CollectionAvatar_collection\n    ...collectionUrl_collection\n    __typename\n  }\n  creator {\n    id\n    username\n    name\n    ...UserAvatar_user\n    ...userUrl_user\n    __typename\n  }\n}\n\nfragment CollectionAvatar_collection on Collection {\n  name\n  avatar {\n    id\n    __typename\n  }\n  ...collectionUrl_collection\n  __typename\n  id\n}\n\nfragment collectionUrl_collection on Collection {\n  id\n  domain\n  slug\n  __typename\n}\n\nfragment UserAvatar_user on User {\n  __typename\n  id\n  imageId\n  mediumMemberAt\n  name\n  username\n  ...userUrl_user\n}\n\nfragment userUrl_user on User {\n  __typename\n  id\n  customDomainState {\n    live {\n      domain\n      __typename\n    }\n    __typename\n  }\n  hasSubdomain\n  username\n}\n\nfragment HomeReadingListItem_post on Post {\n  id\n  title\n  creator {\n    id\n    name\n    username\n    ...UserAvatar_user\n    __typename\n  }\n  mediumUrl\n  createdAt\n  readingTime\n  collection {\n    id\n    name\n    navItems {\n      url\n      __typename\n    }\n    ...CollectionAvatar_collection\n    __typename\n  }\n  visibility\n  __typename\n}\n\nfragment HomeTrendingModule_post on Post {\n  id\n  ...HomeTrendingPostPreview_post\n  __typename\n}\n\nfragment HomeTrendingPostPreview_post on Post {\n  id\n  title\n  mediumUrl\n  readingTime\n  firstPublishedAt\n  ...PostPreviewAvatar_post\n  ...PostPresentationTracker_post\n  __typename\n}\n"}
request=req.Request(url,headers={
    "Content-Typ":"application/json",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
},data=json.dumps(requestData).encode("utf-8")) #encode把charts轉成bytes，送出連線用(編碼)
#發出請求
with req.urlopen(request) as response:
    result=response.read().decode("utf-8") #decode把bytes轉成chars，取得資料時用(解碼)
#解析 JSON 格式的資料，取得每篇文章的標題
print(result)
result=json.loads(result) #把json格式的字串轉換成字典
#print=(result["data"]["extendedFeedItems"]["0"]["post"]["title"])#試著印出第一篇文章的標題
items=result["data"]["extendedFeedItems"]
for item in items:
    print(item["post"]["title"])
#sever error 如請求沒有錯誤那就是伺服器問題