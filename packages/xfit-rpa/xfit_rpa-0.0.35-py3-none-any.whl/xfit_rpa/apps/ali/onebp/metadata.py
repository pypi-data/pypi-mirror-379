live_queryFieldIn = ["LivePromotionScene", "LiveOptimizeTarget", "LiveSmoothType", "LiveDayBudget", "LiveBidType",
                     "LiveGmtCreate", "LiveLaunchTime", "charge", "liveViewNum", "liveViewCost", "adPv", "liveViewRate",
                     "alipayInshopNum", "alipayInshopAmt", "alipayDirAmt", "alipayDirNum", "roi", "dirRoi",
                     "zbInteractCnt", "avgZbInteractCnt", "avgWatchDuration", "favorNumber", "shareNum",
                     "commentsNumber", "followNumber", "followNumberCost", "inshopNum", "feedInshopNumRate",
                     "prepayInshopAmt", "prepayInshopNum", "prepayDirAmt", "prepayDirNum", "cartInshopNum", "colNum",
                     "shoppingNum", "shoppingAmt"]

short_video_queryFieldIn = ["adPv", "click", "roi", "alipayInshopAmt", "charge", "feedViewNum", "ecpc", "ecpm", "ctr",
                            "feedValidViewNum", "feedValidViewCost", "feedValidViewRate", "avgValidVideoWatchDuration",
                            "videoInteractCnt", "videoInteractRate", "videoLiveViewNum", "followNumber",
                            "commentsNumber", "favorNumber", "shareNum", "prepayInshopAmt", "prepayInshopNum",
                            "prepayDirAmt", "prepayDirNum", "prepayIndirAmt", "prepayIndirNum", "gmvInshopAmt",
                            "gmvInshopNum", "alipayInshopNum", "alipayDirAmt", "alipayDirNum", "cvr",
                            "alipayInshopCost", "alipayIndirAmt", "alipayIndirNum", "alipayInshopUv",
                            "alipayInshopNumAvg", "alipayInshopAmtAvg", "itemColCart", "itemColCartCost",
                            "itemColCartRate", "cartInshopNum", "cartDirNum", "cartCost", "itemColInshopNum",
                            "itemColInshopCost", "shopColDirNum", "shopColInshopCost", "colNum", "itemColInshopRate",
                            "itemColDirNum", "itemColIndirNum", "couponShopNum", "shoppingNum", "shoppingAmt",
                            "inshopPv", "inshopUv", "inshopPotentialUv", "inshopPotentialUvRate", "inshopPvRate",
                            "deepInshopPv", "avgAccessPageNum", "rhRate", "rhNum", "hySgUv", "hyPayAmt", "hyPayNum",
                            "newAlipayInshopUv", "liveVideoNewUv", "liveVideoNewCost", "newInshopUv", "interactNewUv",
                            "liveVideoNewAlipayDirAmtRate", "liveVideoNewPrepayDirAmtRate", "makeCharge",
                            "tjmComponentClick", "displayNewCharge", "displayNewInshopNum", "displayNewInshopAmt",
                            "displayNewRoi", "displayNewChargeRate", "firstPurchaseUv", "firstNewCustomerCost",
                            "rseiChargeTotal", "rseiAlipayAmtTotal", "rseiRoiTotal", "rseiCharge", "rseiAlipayAmt",
                            "rseiRoi", "rseiChargeCompete", "rseiAlipayAmtCompete", "rseiRoiCompete"]

union_queryFieldIn = ["UnionGmtCreate", "UnionLaunchTime", "charge", "liveVideoPV", "vedioLiveViewCost", "adPv",
                      "videoliveViewRate", "totalToLiveViewNum", "videoSpotToLiveViewRate", "alipayInshopNum",
                      "alipayInshopAmt", "alipayDirAmt", "alipayDirNum", "roi", "dirRoi", "vedioLiveCvr",
                      "zbInteractCnt", "inshopNum", "liveVideoNewPV", "followNumber", "itemColInshopNum",
                      "cartInshopNum", "prepayInshopAmt", "prepayInshopNum", "prepayDirAmt", "prepayDirNum",
                      "vedioLiveNewUvRate", "liveVideoNewCost", "vedioLiveNewUvCvr", "vedioLiveNewUvRoi",
                      "feedInshopNumRate", "vedioLiveInteractCntRate", "avgZbWatchDuration"]

app_domain = 'https://one.alimama.com'
report_live_url = f'{app_domain}/index.html#!/report/live_migrate?rptType=live_migrate&bizCode=onebpLive'
report_short_video_url = f'{app_domain}/index.html#!/report/short_video_migrate?rptType=short_video_migrate&bizCode=onebpShortVideo'
report_union_url = f'{app_domain}/index.html#!/report/union_migrate?rptType=union_migrate&bizCode=onebpUnion'
page_download_url = f'{app_domain}/index.html#!/report/download-list'
