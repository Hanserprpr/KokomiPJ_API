from ..user_basic import get_user_name_and_clan
from app.log import ExceptionLogger
from app.network import DetailsAPI
from app.response import JSONResponse
from app.models import UserAccessToken

@ExceptionLogger.handle_program_exception_async
async def main(
    account_id: int, 
    region_id: int, 
    language: str, 
    algo_type: str
):
    '''用于`wws me`功能的接口

    返回用户基本数据
    
    '''
    try:
        # 返回数据的格式
        data = {
            'user': {},
            'clan': {},
            'statistics': {}
        }
        # 请求获取user和clan数据
        ac_value = UserAccessToken.get_ac_value_by_id(account_id,region_id)
        user_and_clan_result = await get_user_name_and_clan(
            account_id=account_id,
            region_id=region_id,
            ac_value=ac_value
        )
        if user_and_clan_result['code'] != 1000:
            return user_and_clan_result
        else:
            data['user'] = user_and_clan_result['data']['user']
            data['clan'] = user_and_clan_result['data']['clan']
        # TODO: 获取其他数据
        type_list = ['pvp_solo','pvp_div2','pvp_div3','rank_solo']
        # details_data = await DetailsAPI.get_user_detail(account_id,region_id,type_list,ac_value)
        # for response in details_data:
        #     if response['code'] != 1000:
        #         return response
        # TODO: 数据处理

        # 返回结果
        return JSONResponse.get_success_response(data)
    except Exception as e:
        raise e
