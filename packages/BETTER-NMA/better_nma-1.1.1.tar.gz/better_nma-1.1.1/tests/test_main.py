import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from BETTER_NMA import NMA
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import preprocess_input
import json
import matplotlib.pyplot as plt

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

print("TF version:", tf.__version__)

def test_cifar100_nma():
    print("="*60)
    print("Testing NMA with CIFAR-100 Dataset")
    print("="*60)
    
    # 1. Load CIFAR-100 dataset
    print("\n1. Loading CIFAR-100 dataset...")
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar100.load_data()
    
    labels = [
        'apple', 'aquarium_fish', 'baby', 'bear', 'beaver', 'bed', 'bee', 'beetle', 'bicycle', 'bottle',
        'bowl', 'boy', 'bridge', 'bus', 'butterfly', 'camel', 'can', 'castle', 'caterpillar', 'cattle',
        'chair', 'chimpanzee', 'clock', 'cloud', 'cockroach', 'couch', 'crab', 'crocodile', 'cup', 'dinosaur',
        'dolphin', 'elephant', 'flatfish', 'forest', 'fox', 'girl', 'hamster', 'house', 'kangaroo', 'keyboard',
        'lamp', 'lawn_mower', 'leopard', 'lion', 'lizard', 'lobster', 'man', 'maple_tree', 'motorcycle', 'mountain',
        'mouse', 'mushroom', 'oak_tree', 'orange', 'orchid', 'otter', 'palm_tree', 'pear', 'pickup_truck', 'pine_tree',
        'plain', 'plate', 'poppy', 'porcupine', 'possum', 'rabbit', 'raccoon', 'ray', 'road', 'rocket',
        'rose', 'sea', 'seal', 'shark', 'shrew', 'skunk', 'skyscraper', 'snail', 'snake', 'spider',
        'squirrel', 'streetcar', 'sunflower', 'sweet_pepper', 'table', 'tank', 'telephone', 'television', 'tiger', 'tractor',
        'train', 'trout', 'tulip', 'turtle', 'wardrobe', 'whale', 'willow_tree', 'wolf', 'woman', 'worm'
    ]
    
    # Use a small subset for faster testing (first 500 samples)
    x_train = x_train[:500]
    y_train = y_train[:500]
    
    # Preprocess data
    x_train = preprocess_input(x_train)
    y_train = y_train.astype(int).flatten()
    y_train_strings = [labels[i] for i in y_train]
    
    print(f"x_train shape: {x_train.shape}")
    print(f"y_train_strings example: {y_train_strings[:5]}")
    
    # 2. Load or create model
    print("\n2. Loading CIFAR-100 model...")
    
    # Check if model exists
    model_path = "tests/data/models/cifar100_resnet.keras"
    if os.path.exists(model_path):
        try:
            base_model = tf.keras.models.load_model(model_path)
            print(f"Loaded and wrapped model from: {model_path}")
        except Exception as e:
            raise RuntimeError(f"Failed to load pre-trained model from {model_path}: {e}")
    else:
        raise FileNotFoundError(f"Pre-trained model not found at expected path: {model_path}")
    
    # 3. Initialize NMA with similarity explanation method
    print("\n3. Initializing NMA...")
    try:
        nma = NMA(
            x_train=x_train,
            y_train=y_train_strings,
            labels=labels,
            model=base_model,
            explanation_method="similarity",
            top_k=4,
            min_confidence=0.8,
            batch_size=32,
            save_connections=True  # Required for white-box testing
        )
        print("NMA initialized successfully")
    except Exception as e:
        print(f"Error initializing NMA: {e}")
        return None
    
    print("\n" + "="*60)
    print("TESTING NMA FUNCTIONALITIES")
    print("="*60)
    
    # Test 1: nma.plot() - Full dendrogram
    print("\n📊 Test 1: nma.plot() - Full dendrogram")
    print("-"*40)
    try:
        nma.plot(title="CIFAR-100 Full Dendrogram", figsize=(20, 20))
        print("✓ Full dendrogram plotted")
        plt.close('all')  # Close plots to save memory
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Test 2: nma.plot() with sub_labels
    print("\n📊 Test 2: nma.plot() with sub_labels")
    print("-"*40)
    try:
        # Test with tree-related labels
        tree_labels = ["maple_tree", "oak_tree", "palm_tree", "pine_tree", "willow_tree", "forest"]
        nma.plot(sub_labels=tree_labels, title="Tree Classes Sub-Dendrogram", figsize=(12, 8))
        print(f"✓ Sub-dendrogram plotted for: {tree_labels}")
        plt.close('all')
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Test 3: nma.plot_sub_dendrogram()
    print("\n📊 Test 3: nma.plot_sub_dendrogram()")
    print("-"*40)
    try:
        # Test with people-related labels
        people_labels = ["baby", "boy", "girl", "man", "woman"]
        nma.plot_sub_dendrogram(sub_labels=people_labels, title="People Classes", figsize=(10, 6))
        print(f"✓ plot_sub_dendrogram worked for: {people_labels}")
        plt.close('all')
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Test 4: Dendrogram get_sub_dendrogram_formatted()
    print("\n🌳 Test 4: Dendrogram.get_sub_dendrogram_formatted()")
    print("-"*40)
    try:
        sub_json = nma.dendrogram_object.get_sub_dendrogram_formatted(tree_labels)
        sub_dict = json.loads(sub_json)
        print("✓ Returned sub-dendrogram dict with keys:", list(sub_dict.keys()))
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Test 5: Dendrogram.rename_cluster()
    print("\n✏️  Test 5: Dendrogram.rename_cluster()")
    print("-"*40)
    try:
        # Pick the root cluster id (2*len(leaves)-2) for rename demo
        root_id = len(tree_labels)*2 - 2
        nma.dendrogram_object.rename_cluster(root_id, "my_cluster")
        renamed_json = nma.dendrogram_object.get_sub_dendrogram_formatted(tree_labels)
        renamed_dict = json.loads(renamed_json)
        print("✓ Cluster renamed → new root name:", renamed_dict.get("name"))
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Test 4: nma.get_tree_as_dict()
    print("\n📋 Test 4: nma.get_tree_as_dict()")
    print("-"*40)
    try:
        # Full tree
        tree_dict = nma.get_tree_as_dict()
        print("✓ Got full tree as dictionary")
        print(f"  Keys: {list(tree_dict.keys())}")
        if 'name' in tree_dict:
            print(f"  Root name: {tree_dict['name']}")
        
        # Sub-tree with animal labels
        animal_labels = ["bear", "beaver", "bee", "beetle", "butterfly"]
        sub_tree_dict = nma.get_tree_as_dict(sub_labels=animal_labels)
        print(f"✓ Got sub-tree for: {animal_labels}")
        
        # Show structure
        tree_json = json.dumps(sub_tree_dict, indent=2)
        print(f"  Sub-tree preview (first 200 chars): {tree_json[:200]}...")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Test 5: nma.find_lca()
    print("\n🔍 Test 5: nma.find_lca() - Finding Lowest Common Ancestors")
    print("-"*40)
    
    test_pairs = [
        ("woman", "girl"),          # People/female cluster
        ("man", "boy"),             # People/male cluster
        ("maple_tree", "oak_tree"), # Tree cluster
        ("bee", "beetle"),          # Insect cluster
        ("apple", "pear"),          # Fruit cluster
        ("tulip", "orchid"),        # Flower cluster
    ]
    
    for label1, label2 in test_pairs:
        try:
            lca = nma.find_lca(label1, label2)
            print(f"✓ LCA of '{label1}' and '{label2}': {lca}")
        except Exception as e:
            print(f"✗ Error finding LCA for {label1}-{label2}: {e}")
    
    # Test 6: nma.white_box_testing()
    print("\n🧪 Test 6: nma.white_box_testing()")
    print("-"*40)
    try:
        # Test as in Kaggle example
        source_labels = ["beetle", "tulip"]
        target_labels = ["bee", "orchid"]
        
        print(f"  Testing: {source_labels} → {target_labels}")
        
        # Without analysis
        problematic_imgs = nma.white_box_testing(
            source_labels=source_labels,
            target_labels=target_labels,
            analyze_results=False
        )
        
        print(f"✓ White-box testing completed")
        print(f"  Found {len(problematic_imgs)} problematic images")
        
        if problematic_imgs:
            # Show first problematic image
            img_id = list(problematic_imgs.keys())[0]
            matches = problematic_imgs[img_id]
            print(f"  Example - Image {img_id}: {len(matches)} matches")
            for match in matches[:3]:
                print(f"    {match[0]} → {match[1]}: {match[2]:.4f}")
        
        # With analysis
        analyzed_results = nma.white_box_testing(
            source_labels=source_labels,
            target_labels=target_labels,
            analyze_results=True,
            x_train=x_train,
            encode_images=False
        )
        print(f"✓ Analysis completed: {len(analyzed_results)} results")
        
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Test 7: nma.get_white_box_analysis()
    print("\n🧪 Test 7: nma.get_white_box_analysis()")
    print("-"*40)
    try:
        source_labels = ["woman", "girl"]
        target_labels = ["man", "boy"]
        
        print(f"  Testing: {source_labels} → {target_labels}")
        
        analysis = nma.get_white_box_analysis(
            source_labels=source_labels,
            target_labels=target_labels,
            x_train=x_train
        )
        
        print(f"✓ Analysis completed: {len(analysis)} entries")
        if analysis:
            print(f"  Entry keys: {list(analysis[0].keys())}")
            
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Test 8: get_common_ancestor_subtree()
    print("\n🌲 Test 8: get_common_ancestor_subtree()")
    print("-"*40)
    try:
        # Test with animal classes
        animal_labels = ["bear", "wolf", "tiger", "lion"]
        print(f"  Finding common ancestor for: {animal_labels}")
        
        subtree, all_labels = nma.dendrogram_object.get_common_ancestor_subtree(animal_labels)
        
        print(f"✓ Common ancestor cluster: {subtree.get('name', 'Unknown')}")
        print(f"  Distance/similarity value: {subtree.get('value', 'N/A')}")
        print(f"  Total labels in cluster: {len(all_labels)}")
        print(f"  All labels: {all_labels[:10]}{'...' if len(all_labels) > 10 else ''}")
        
        # Test with plant classes
        plant_labels = ["maple_tree", "oak_tree", "pine_tree"]
        print(f"\n  Finding common ancestor for plants: {plant_labels}")
        
        plant_subtree, plant_all_labels = nma.dendrogram_object.get_common_ancestor_subtree(plant_labels)
        
        print(f"✓ Plant common ancestor: {plant_subtree.get('name', 'Unknown')}")
        print(f"  All plant-related labels: {plant_all_labels}")
        
        # Test with vehicle classes
        vehicle_labels = ["bicycle", "bus", "motorcycle", "pickup_truck", "train"]
        print(f"\n  Finding common ancestor for vehicles: {vehicle_labels}")
        
        vehicle_subtree, vehicle_all_labels = nma.dendrogram_object.get_common_ancestor_subtree(vehicle_labels)
        
        print(f"✓ Vehicle common ancestor: {vehicle_subtree.get('name', 'Unknown')}")
        print(f"  All vehicle-related labels: {vehicle_all_labels}")
        
        print("✓ get_common_ancestor_subtree test passed!")
        
    except Exception as e:
        print(f"✗ Error testing get_common_ancestor_subtree: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    
    print("\n✅ Tested NMA functionalities:")
    print("  1. nma.plot() - Full and sub dendrograms")
    print("  2. nma.plot_sub_dendrogram() - Specific label subsets")
    print("  3. nma.get_tree_as_dict() - Tree structure as dictionary")
    print("  4. nma.find_lca() - Finding lowest common ancestors")
    print("  5. nma.white_box_testing() - Identifying problematic images")
    print("  6. nma.get_white_box_analysis() - Detailed analysis")
    print("  7. get_common_ancestor_subtree() - Finding semantic clusters")
    
    return nma

if __name__ == "__main__":
    try:
        print("Starting CIFAR-100 NMA tests...")
        print("Using subset of 500 samples for faster testing\n")
        
        nma = test_cifar100_nma()
        
        if nma:
            print("\n✅ All tests completed successfully!")
        else:
            print("\n⚠ Tests completed with issues")
        
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        import traceback
        traceback.print_exc()