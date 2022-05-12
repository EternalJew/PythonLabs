using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using UnityEngine.UI;


public class PostMe : MonoBehaviour
{
    //QUEST
    public InputField quest_name;
    public InputField quest_description;
    public InputField questReqLvl;
    public InputField list_of_tasks;
    public InputField quest_reward_coins;
    public InputField quest_reward_XP;
    
    //TASK
    public InputField task_name;
    public InputField task_description;
    public InputField task_reward_coins;
    public InputField task_reward_XP;
    public InputField npc_name;
    public InputField npc_phrase;
    public InputField player_variant_answer;
    public InputField npc_answer;

    //ASSET
    public InputField asset_bundle_name;
    public InputField bundle_name;
    public InputField asset_name;




    [Serializable]
    public class Quest
    {
        //QUEST
        public string quest_name;
        public string quest_description;
        public int quest_required_lvl;
        public string list_of_tasks;
        public int quest_reward_coins;
        public int quest_reward_XP;

        //TASK
        public string task_name;
        public string task_description;
        public int task_reward_coins;
        public int task_reward_XP;
        public string npc_name;
        public string npc_phrase;
        public string player_variant_answer;
        public string npc_answer;
        
        //ASSET
        public string asset_bundle_name;
        public string bundle_name;
        public string asset_name;


    }

    public void PostData()
    {
        //QUEST
        string quest_name_FromInput = quest_name.text;
        string quest_description_FromInput = quest_description.text;
        int quest_required_lvl_FromInput = Int32.Parse(quest_required_lvl.text);
        string list_of_tasks_FromInput = list_of_tasks.text;
        int quest_reward_coins_FromInput = Int32.Parse(quest_reward_coins.text);
        int quest_reward_XP_FromInput = Int32.Parse(quest_reward_XP.text);
        //TASK
        string task_name_FromInput = task_name.text;
        string task_description_FromInput = task_description.text;
        int task_reward_coins_FromInput = Int32.Parse(task_reward_coins.text);
        int task_reward_XP_FromInput = Int32.Parse(task_reward_XP.text);
        string npc_name_FromInput = npc_name.text;
        string npc_phrase_FromInput = npc_phrase.text;
        string player_variant_answer_FromInput = player_variant_answer.text;
        string npc_answer_FromInput = npc_answer.text;

        //ASSET
        string asset_bundle_name_FromInput = asset_bundle_name.text;
        string bundle_name_FromInput = bundle_name.text;
        string asset_name_FromInput = asset_name.text;


        //QUEST
        Quest quest = new Quest();
        quest.quest_name = quest_name_FromInput;
        quest.quest_description = quest_description_FromInput;
        quest.quest_required_lvl = quest_required_lvl_FromInput;
        quest.list_of_tasks = list_of_tasks_FromInput;
        quest.quest_reward_coins = quest_reward_coins_FromInput;
        quest.quest_reward_XP = quest_reward_XP_FromInput;
        //TASK
        quest.task_name = task_name_FromInput;
        quest.task_description = task_description_FromInput;
        quest.task_reward_coins = task_reward_coins_FromInput;
        quest.task_reward_XP = task_reward_XP_FromInput;
        quest.npc_name = npc_name_FromInput;
        quest.npc_phrase = npc_phrase_FromInput;
        quest.player_variant_answer = player_variant_answer_FromInput;
        quest.npc_answer = npc_answer_FromInput;

        //ASSET
        quest.asset_bundle_name = asset_bundle_name_FromInput;
        quest.bundle_name = bundle_name_FromInput;
        quest.asset_name = asset_name_FromInput;


        string json = JsonUtility.ToJson(quest);
        StartCoroutine(PostRequest("http://127.0.0.1:5000/list_add", json));
    }

    IEnumerator PostRequest(string url, string json)
    {
        var uwr = new UnityWebRequest(url, "POST");
        byte[] jsonToSend = new System.Text.UTF8Encoding().GetBytes(json);
        uwr.uploadHandler = (UploadHandler)new UploadHandlerRaw(jsonToSend);
        uwr.downloadHandler = (DownloadHandler)new DownloadHandlerBuffer();
        uwr.SetRequestHeader("Content-Type", "application/json");

        //Send the request then wait here until it returns
        yield return uwr.SendWebRequest();

        if (uwr.result == UnityWebRequest.Result.ConnectionError)
        {
            Debug.Log("Error While Sending: " + uwr.error);
        }
        else
        {
            Debug.Log("Received: " + uwr.downloadHandler.text);
        }

    }
}
