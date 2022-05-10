using UnityEngine;
using UnityEngine.Networking;
using System.Collections;
using System.Linq;

public class GetBundleTest : MonoBehaviour
{
    public void Start() {
        StartCoroutine(GetAssetBundle());
    }
 
    IEnumerator GetAssetBundle() {
            var assetBundles = AssetBundle.GetAllLoadedAssetBundles().ToList();
            var assetBundle = assetBundles.Find(x => x.name == "q1");

            if(assetBundle != null)
            {
                Debug.Log("laoded cached data");
                yield break;
            }

        UnityWebRequest www = UnityWebRequestAssetBundle.GetAssetBundle("http://0.0.0.0:5005/static/q1.unity3d");
        yield return www.SendWebRequest();
 
        if (www.result != UnityWebRequest.Result.Success) {
            Debug.Log(www.error);
        }
        else {
            AssetBundle bundle = DownloadHandlerAssetBundle.GetContent(www);
        }
    }
}
