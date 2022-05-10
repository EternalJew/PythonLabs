using UnityEngine;
using UnityEngine.Networking;
using System.Threading.Tasks;

[System.Serializable]
    public struct Vector2String
    {
        public string x;
        public string y;

        public Vector2String(string x, string y)
        {
            this.x = x;
            this.y = y;
        }
    }

public class test : MonoBehaviour
{

    private void Awake() {
        Test();
    }

    public async void Test()
    {
        const string BUNDLE_NAME = "q1";
        const string ASSET_NAME = "t1";

        var obj = await GetBundleObject(new Vector2String(BUNDLE_NAME, ASSET_NAME));
        Debug.Log(obj);
    }
    
    public async Task<object> GetBundleObject(Vector2String bundle)//(bundleName, assetName)
        {
            string bundleURL = "BundleFolder" + bundle.x + "-";

            //append platform to asset bundle name
#if UNITY_ANDROID
            bundleURL += "Android";
#else
            bundleURL += "IOS";
#endif

            Debug.Log("Requesting bundle at " + bundleURL);

            using (UnityWebRequest uwr = UnityWebRequestAssetBundle.GetAssetBundle(bundleURL + ".unity3d"))
            {
                var operaion = uwr.SendWebRequest();

                while (!operaion.isDone)
                    await Task.Yield();

                if (uwr.result != UnityWebRequest.Result.Success)
                {
                    Debug.Log(uwr.error);
                    return default;
                }

                Debug.Log("Bundle is loaded");

                AssetBundle loadedbNndle = DownloadHandlerAssetBundle.GetContent(uwr);
                var loadAsset = loadedbNndle.LoadAssetAsync(bundle.y);

                while (!loadAsset.isDone)
                    await Task.Yield();

                return loadAsset.asset;
            }
        }
}
