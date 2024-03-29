SELECT II.ITEM_ID, II.ITEM_NAME, II.RARITY
FROM ITEM_INFO II, ITEM_TREE IT
WHERE IT.PARENT_ITEM_ID IN (SELECT II.ITEM_ID
                            FROM ITEM_INFO II, ITEM_TREE IT
                            WHERE II.RARITY = 'RARE'
                            AND II.ITEM_ID = IT.ITEM_ID)
ORDER BY II.ITEM_ID DESC