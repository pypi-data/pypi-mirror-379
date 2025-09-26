from ..exceptions import APIException

async def answer_callback_query(client, callback_query_id, **kwargs):
    """Send answers to callback queries"""
    try:
        payload = {
            'callback_query_id': callback_query_id,
            **kwargs
        }
        
        result = await client._make_request('answerCallbackQuery', payload)
        return result.get('ok', False)
    except Exception as e:
        raise APIException(f"Failed to answer callback query: {e}")
