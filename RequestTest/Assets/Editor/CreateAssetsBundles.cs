using UnityEngine;
using UnityEditor;

public class CreateAssetsBundles{
    [MenuItem("Assets/Build AssetBundless")]
   static void BuildAllAssetsBundles()
   {
       BuildPipeline.BuildAssetBundles("Assets/AssetBundles", BuildAssetBundleOptions.None, BuildTarget.StandaloneWindows64);
   }
}
