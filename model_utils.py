import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

MODEL_DIR = "./big5-bert-normalized-model"

device = torch.device("cpu")  

tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_DIR)
model.to(device)
model.eval()

trait_names = ["agreeableness", "openness", "conscientiousness", "extraversion", "neuroticism"]

mins = {"agreeableness":0,"openness":9,"conscientiousness":1,"extraversion":0,"neuroticism":0}
maxs = {"agreeableness":99,"openness":98,"conscientiousness":98,"extraversion":99,"neuroticism":99}

def denormalize(val, trait):
    return val * (maxs[trait] - mins[trait]) + mins[trait]

def level_from_score(score: float) -> str:
    """Convert 0–100 score into Low / Medium / High."""
    if score < 40:
        return "Low"
    elif score < 60:
        return "Medium"
    else:
        return "High"

def summarize_personality(scores: dict) -> str:
    """Generate a short, simple summary sentence/paragraph."""
    # sort traits from high to low
    sorted_traits = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    top_trait, top_score = sorted_traits[0]
    second_trait, second_score = sorted_traits[1]

    # simple phrases
    nice_names = {
        "agreeableness": "kind and cooperative",
        "openness": "curious and imaginative",
        "conscientiousness": "organized and responsible",
        "extraversion": "outgoing and energetic",
        "neuroticism": "emotionally sensitive"
    }

    if top_trait == "neuroticism":
        return (
            "You seem emotionally sensitive and may experience feelings quite deeply. "
            f"You also show relatively higher {second_trait}, which suggests you might be {nice_names.get(second_trait, second_trait)} in many situations."
        )
    else:
        return (
            f"Your strongest trait here is {top_trait} ({top_score:.1f}), "
            f"suggesting you tend to be {nice_names.get(top_trait, top_trait)}. "
            f"You also show noticeable {second_trait}, which adds a mix of {nice_names.get(second_trait, second_trait)} to your personality."
        )

@torch.no_grad()
def predict_personality(text: str):
    if not text.strip():
        return {}, {}, ""

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=256
    )
    inputs = {k: v.to(device) for k, v in inputs.items()}

    outputs = model(**inputs)
    norm_scores = outputs.logits.squeeze().cpu().tolist()  # 0–1

    # back to ~0–100 scale
    raw_scores = {
        trait: float(f"{denormalize(score, trait):.2f}")
        for trait, score in zip(trait_names, norm_scores)
    }

    levels = {
        trait: level_from_score(score)
        for trait, score in raw_scores.items()
    }

    summary = summarize_personality(raw_scores)

    # return everything so UI can use it
    return raw_scores, levels, summary
