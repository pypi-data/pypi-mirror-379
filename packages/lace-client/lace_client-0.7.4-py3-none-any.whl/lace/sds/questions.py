"""
EU AI Act SDS Question Set - Canonical questions for template completion.
"""

SDS_QUESTIONS = [
    # Section 1.1 - Provider identification
    {
        "id": "provider.name",
        "text": "Provider name",
        "type": "text",
        "required": True,
        "section": "1.1",
        "help": "Legal name of the organization providing the model",
    },
    {
        "id": "provider.contact",
        "text": "Provider contact email",
        "type": "email",
        "required": True,
        "section": "1.1",
        "help": "Main contact email for compliance matters",
    },
    {
        "id": "provider.eu_representative",
        "text": "Is your organization established outside the EU?",
        "type": "yesno",
        "required": True,
        "section": "1.1",
        "help": "If yes, you'll need to provide EU representative details",
    },
    {
        "id": "provider.eu_rep_name",
        "text": "EU authorized representative name",
        "type": "text",
        "required_if": "provider.eu_representative == yes",
        "section": "1.1",
    },
    {
        "id": "provider.eu_rep_contact",
        "text": "EU authorized representative contact email",
        "type": "email",
        "required_if": "provider.eu_representative == yes",
        "section": "1.1",
    },
    # Section 1.2 - Model identification
    {
        "id": "model.name",
        "text": "Model name(s) and version(s)",
        "type": "text",
        "required": True,
        "section": "1.2",
        "help": "e.g., 'Llama-3.1-8B-Instruct v2' or comma-separated if multiple",
    },
    {
        "id": "model.dependencies",
        "text": "Is this model based on/fine-tuned from another model?",
        "type": "yesno",
        "required": True,
        "section": "1.2",
    },
    {
        "id": "model.base_model",
        "text": "Base model name and link to its SDS (if available)",
        "type": "text",
        "required_if": "model.dependencies == yes",
        "section": "1.2",
    },
    {
        "id": "model.placed_on_market",
        "text": "Date placed on EU market (YYYY-MM)",
        "type": "date-ym",
        "required": True,
        "section": "1.2",
        "help": "When the model became available for use in the EU",
    },
    {
        "id": "model.card_url",
        "text": "Model card or documentation URL (optional)",
        "type": "url",
        "required": False,
        "section": "1.2",
    },
    # Section 1.3 - Training characteristics
    {
        "id": "training.continuous",
        "text": "Is the model continuously trained on new data after the latest acquisition date?",
        "type": "yesno",
        "required": True,
        "section": "1.3",
    },
    {
        "id": "training.other_characteristics",
        "text": "Other relevant training data characteristics (optional)",
        "type": "textarea",
        "required": False,
        "section": "1.3",
        "help": "e.g., national/regional specifics, demographic characteristics",
    },
    # Section 2.1 - Public datasets
    {
        "id": "sources.public_confirm",
        "text": "Were publicly available datasets used for training?",
        "type": "yesno",
        "required": True,
        "section": "2.1",
    },
    {
        "id": "sources.public_selection",
        "text": "If only parts of datasets were used, describe the selection approach",
        "type": "text",
        "required_if": "sources.public_confirm == yes",
        "section": "2.1",
        "help": "e.g., 'Random 10% sample' or 'English content only'",
    },
    # Section 2.2 - Private datasets
    {
        "id": "sources.licensed",
        "text": "Were commercially licensed datasets used?",
        "type": "yesno",
        "required": True,
        "section": "2.2.1",
    },
    {
        "id": "sources.licensed_modalities",
        "text": "Modalities of licensed content",
        "type": "multiselect",
        "options": ["text", "image", "audio", "video", "other"],
        "required_if": "sources.licensed == yes",
        "section": "2.2.1",
    },
    {
        "id": "sources.other_private",
        "text": "Were other private datasets (not commercially licensed) used?",
        "type": "yesno",
        "required": True,
        "section": "2.2.2",
    },
    {
        "id": "sources.other_private_description",
        "text": "Describe the private datasets",
        "type": "textarea",
        "required_if": "sources.other_private == yes",
        "section": "2.2.2",
    },
    # Section 2.3 - Provider crawling (CRITICAL GATE)
    {
        "id": "sources.provider_crawled",
        "text": "Did you (or vendors on your behalf) run web crawlers to collect training data?",
        "type": "yesno",
        "required": True,
        "section": "2.3",
        "help": "This excludes using pre-existing datasets like Common Crawl",
    },
    {
        "id": "sources.crawler_names",
        "text": "Crawler name(s)/identifier(s)",
        "type": "text",
        "required_if": "sources.provider_crawled == yes",
        "section": "2.3",
    },
    {
        "id": "sources.crawler_purpose",
        "text": "Purpose of crawling",
        "type": "text",
        "required_if": "sources.provider_crawled == yes",
        "section": "2.3",
    },
    {
        "id": "sources.crawler_period",
        "text": "Crawling period (MM/YYYY to MM/YYYY)",
        "type": "text",
        "required_if": "sources.provider_crawled == yes",
        "section": "2.3",
        "help": "e.g., '01/2023 to 06/2024'",
    },
    {
        "id": "sources.crawler_behavior",
        "text": "How did crawlers handle robots.txt, captchas, paywalls?",
        "type": "textarea",
        "required_if": "sources.provider_crawled == yes",
        "section": "2.3",
    },
    {
        "id": "sources.crawled_types",
        "text": "Types of websites crawled",
        "type": "text",
        "required_if": "sources.provider_crawled == yes",
        "section": "2.3",
        "help": "e.g., news sites, blogs, forums, educational sites",
    },
    # Section 2.4 - User data
    {
        "id": "sources.user_interactions",
        "text": "Was data from user interactions with the model used for training?",
        "type": "yesno",
        "required": True,
        "section": "2.4",
    },
    {
        "id": "sources.user_services",
        "text": "Was data from your other services/products used for training?",
        "type": "yesno",
        "required": True,
        "section": "2.4",
    },
    {
        "id": "sources.user_description",
        "text": "Describe the services/products that collected user data",
        "type": "textarea",
        "required_if": "sources.user_services == yes",
        "section": "2.4",
    },
    # Section 2.5 - Synthetic data
    {
        "id": "sources.synthetic",
        "text": "Was synthetic AI-generated data used for training?",
        "type": "yesno",
        "required": True,
        "section": "2.5",
    },
    {
        "id": "sources.synthetic_models",
        "text": "Which model(s) generated the synthetic data?",
        "type": "text",
        "required_if": "sources.synthetic == yes",
        "section": "2.5",
        "help": "Model names and links to their SDSs if available",
    },
    # Section 2.6 - Other sources
    {
        "id": "sources.other",
        "text": "Were any other data sources used not covered above?",
        "type": "yesno",
        "required": True,
        "section": "2.6",
    },
    {
        "id": "sources.other_description",
        "text": "Describe the other data sources",
        "type": "textarea",
        "required_if": "sources.other == yes",
        "section": "2.6",
    },
    # Section 3.1 - TDM opt-out
    {
        "id": "processing.code_signatory",
        "text": "Are you a signatory to the GPAI Code of Practice?",
        "type": "yesno",
        "required": True,
        "section": "3.1",
    },
    {
        "id": "processing.tdm_measures",
        "text": "Describe additional TDM opt-out measures beyond our detected signals",
        "type": "textarea",
        "required": False,
        "section": "3.1",
        "help": "We've detected robots.txt/ai.txt compliance. Add any other measures.",
    },
    {
        "id": "processing.copyright_policy_url",
        "text": "Link to your public copyright policy (optional)",
        "type": "url",
        "required": False,
        "section": "3.1",
    },
    # Section 3.2 - Illegal content removal
    {
        "id": "processing.content_measures",
        "text": "Select content filtering measures used",
        "type": "multiselect",
        "options": [
            "keyword_blacklists",
            "hash_matching",
            "ml_classifiers",
            "manual_review",
            "deduplication",
            "trusted_flagging",
            "none",
        ],
        "required": True,
        "section": "3.2",
        "help": "Check all that apply",
    },
    {
        "id": "processing.content_description",
        "text": "Briefly describe your content filtering approach",
        "type": "textarea",
        "required": True,
        "section": "3.2",
        "help": "1-2 sentences on how illegal content is detected and removed",
    },
]


def get_required_questions(answers: dict = None) -> list:
    """
    Get list of questions that should be asked based on conditional logic.

    Args:
        answers: Dictionary of already provided answers

    Returns:
        List of question dicts that should be asked
    """
    answers = answers or {}
    required = []

    for question in SDS_QUESTIONS:
        # Check if question should be asked
        if "required_if" in question:
            # Parse condition (simple format: "field == value")
            condition = question["required_if"]
            if "==" in condition:
                field, value = condition.split(" == ")
                field = field.strip()
                value = value.strip()

                # Check if condition is met
                if answers.get(field) == value:
                    required.append(question)
            else:
                # More complex conditions would go here
                pass
        elif question.get("required", False):
            # Always required
            required.append(question)
        else:
            # Optional questions
            required.append(question)

    return required


def validate_answer(question: dict, answer: str) -> tuple[bool, str]:
    """
    Validate an answer based on question type.

    Args:
        question: Question dictionary
        answer: User's answer

    Returns:
        Tuple of (is_valid, error_message)
    """
    q_type = question.get("type", "text")

    if q_type == "email":
        # Basic email validation
        import re

        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", answer):
            return False, "Invalid email format"

    elif q_type == "date-ym":
        # YYYY-MM format
        import re

        if not re.match(r"^\d{4}-(0[1-9]|1[0-2])$", answer):
            # Also accept MM/YYYY and convert
            if re.match(r"^(0[1-9]|1[0-2])/\d{4}$", answer):
                return True, ""
            return False, "Date must be in YYYY-MM or MM/YYYY format"

    elif q_type == "yesno":
        if answer.lower() not in ["yes", "no", "y", "n"]:
            return False, "Answer must be yes/no or y/n"

    elif q_type == "url":
        # Basic URL validation
        if answer and not (
            answer.startswith("http://") or answer.startswith("https://")
        ):
            return False, "URL must start with http:// or https://"

    elif q_type == "multiselect":
        # Check against valid options
        options = question.get("options", [])
        selected = [s.strip() for s in answer.split(",")]
        invalid = [s for s in selected if s not in options]
        if invalid:
            return False, f"Invalid options: {', '.join(invalid)}"

    return True, ""
