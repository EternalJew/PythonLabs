using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using UnityEngine.UI;


public class PostMe : MonoBehaviour
{
    public InputField questID;
    public InputField questName;
    public InputField questDesc;
    public InputField questReqLvl;

    [Serializable]
    public class Quest
    {
        public int questID;
        public string questName;
        public string questDesc;
        public int questReqLvl;
    }

    public void PostData()
    {
        int questIDFromInput = Int32.Parse(questID.text);
        string questNameFromInput = questName.text;
        string questDescFromInput = questDesc.text;
        int questReqLvlFromInput = Int32.Parse(questReqLvl.text);

        Quest quest = new Quest();
        quest.questID = questIDFromInput;
        quest.questName = questNameFromInput;
        quest.questDesc = questDescFromInput;
        quest.questReqLvl = questReqLvlFromInput;

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
