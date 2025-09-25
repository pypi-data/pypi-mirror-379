# EU AI Act Public Summary of Training Content - Answer Keys
## Version: v2025_09

This document defines all answer keys for the EU AI Act Article 53(1)(d) compliance template.

### Principles
- **Tri-state fields**: Sections 2.1-2.6 use "Yes"/"No"/"TO_BE_PROVIDED" 
- **Never auto-infer**: Tool never guesses Yes/No based on evidence
- **User-provided only**: Attestational fields require explicit user input
- **Neutral placeholders**: Use "TO BE PROVIDED" for required fields without data

---

## Header Fields

| Key | Type | Description | Default |
|-----|------|-------------|---------|
| `summary_version` | string | Version of the summary document | "v0.1" |
| `last_update` | string | ISO date of last update (YYYY-MM-DD) | Current date |

---

## Section 1.1: Provider Identification

| Key | Type | Description | Default |
|-----|------|-------------|---------|
| `provider_name` | string | Name of the provider organization | "TO BE PROVIDED" |
| `provider_contact` | string | Contact information (email/website) | "TO BE PROVIDED" |
| `authorized_rep_name` | string | Authorized representative name (if outside EU) | "Not applicable" |
| `authorized_rep_contact` | string | Authorized representative contact | "" |

---

## Section 1.2: Model Identification

| Key | Type | Description | Default |
|-----|------|-------------|---------|
| `model_name` | string | Versioned model name | "TO BE PROVIDED" |
| `model_dependencies` | array | List of model dependencies [{name, link}] | [] |
| `date_placement_eu` | string | Date placed on EU market (YYYY-MM-DD) | "TO BE PROVIDED" |

---

## Section 1.3: Modalities, Size, and Characteristics

### Modalities (boolean flags)
| Key | Type | Description | Source |
|-----|------|-------------|--------|
| `modalities.text` | boolean | Text data present | From scan |
| `modalities.image` | boolean | Image data present | From scan |
| `modalities.audio` | boolean | Audio data present | From scan |
| `modalities.video` | boolean | Video data present | From scan |

### Size Bands
| Key | Type | Description | Values |
|-----|------|-------------|--------|
| `size_bands.text` | string | Text data size band | "<1B tokens" / "1B-10T tokens" / ">10T tokens" / "Not known" / "N/A" |
| `size_bands.image` | string | Image data size band | "<1M images" / "1M-1B images" / ">1B images" / "Not known" / "N/A" |
| `size_bands.audio` | string | Audio data size band | "<10K hours" / "10K-1M hours" / ">1M hours" / "Not known" / "N/A" |
| `size_bands.video` | string | Video data size band | "<10K hours" / "10K-1M hours" / ">1M hours" / "Not known" / "N/A" |

### Content Types
| Key | Type | Description | Default |
|-----|------|-------------|---------|
| `types_of_content.text` | string | Types of text content | "TO BE PROVIDED" or includes "source code" if detected |
| `types_of_content.image` | string | Types of image content | "" |
| `types_of_content.audio` | string | Types of audio content | "" |
| `types_of_content.video` | string | Types of video content | "" |

### Other Characteristics
| Key | Type | Description | Source |
|-----|------|-------------|--------|
| `latest_acquisition_mm_yyyy` | string | Latest data acquisition (MM/YYYY) | From scan or "TO BE PROVIDED" |
| `language_summary` | string | Language distribution summary | From scan or "TO BE PROVIDED" |
| `other_overall_characteristics` | string | Other relevant characteristics | User-provided or "" |

---

## Section 2.1: Publicly Available Datasets

| Key | Type | Description | Default |
|-----|------|-------------|---------|
| `public_datasets_used` | string | Whether public datasets used | "TO_BE_PROVIDED" (tri-state) |
| `public_datasets_modalities` | array | Modalities of public datasets ["text","image",...] | [] |
| `public_datasets_large` | array | Large datasets (≥3% share) [{name, link, modality}] | From scan if confirmed |
| `public_datasets_other_desc` | string | Description of other public datasets | "" |

---

## Section 2.2: Private Datasets (Licensed and Other Third Parties)

| Key | Type | Description | Default |
|-----|------|-------------|---------|
| `licensed_datasets_used` | string | Whether licensed datasets used | "TO_BE_PROVIDED" (tri-state) |
| `licensed_datasets_modalities` | array | Modalities of licensed datasets | [] |
| `other_private_datasets_used` | string | Whether other private datasets used | "TO_BE_PROVIDED" (tri-state) |
| `other_private_datasets_modalities` | array | Modalities of other private datasets | [] |
| `other_private_datasets_list_publicly_known` | array | List of known private datasets | [] |
| `other_private_datasets_general_description` | string | General description | "" |

---

## Section 2.3: Data Obtained via Web Crawlers

**CRITICAL**: Only set to "Yes" if user explicitly confirms crawler use. Never infer from domain evidence.

| Key | Type | Description | Default |
|-----|------|-------------|---------|
| `crawlers_used` | string | Whether crawlers were used | "TO_BE_PROVIDED" (tri-state) |
| `crawler_names` | array | Crawler identifiers/names | [] |
| `crawler_purposes` | string | Purpose of crawling | "" |
| `crawler_behavior` | string | Crawler behavior (robots, captcha, paywalls) | "" |
| `crawler_period_start_mm_yyyy` | string | Crawling period start (MM/YYYY) | "" |
| `crawler_period_end_mm_yyyy` | string | Crawling period end (MM/YYYY) | "" |
| `crawler_sources_description` | string | Types of sources crawled | "" |
| `crawler_modalities` | array | Modalities from crawling | [] |
| `crawled_domains_csv_path` | string | Path to top domains CSV (generated if crawlers_used=Yes) | Added by CLI |

---

## Section 2.4: User Data

| Key | Type | Description | Default |
|-----|------|-------------|---------|
| `used_user_interactions_for_training` | string | User interactions used | "TO_BE_PROVIDED" (tri-state) |
| `used_other_provider_services_for_training` | string | Other services data used | "TO_BE_PROVIDED" (tri-state) |
| `user_services_description` | string | Description of user services | "" |
| `user_data_modalities` | array | Modalities from user data | [] |

---

## Section 2.5: Synthetic Data

| Key | Type | Description | Default |
|-----|------|-------------|---------|
| `synthetic_data_used` | string | Whether synthetic data used | "TO_BE_PROVIDED" (tri-state) |
| `synthetic_modalities` | array | Modalities of synthetic data | [] |
| `synthetic_models_used_public` | array | Public models used [{name, link}] | [] |
| `synthetic_models_used_internal_description` | string | Internal models description | "" |

---

## Section 2.6: Other Sources

| Key | Type | Description | Default |
|-----|------|-------------|---------|
| `other_sources_used` | string | Whether other sources used | "TO_BE_PROVIDED" (tri-state) |
| `other_sources_description` | string | Description of other sources | "" |

---

## Section 3.1: Respect of Reservation of Rights (TDM Opt-Out)

| Key | Type | Description | Default |
|-----|------|-------------|---------|
| `tdm_signatory` | boolean | Signatory to Code of Practice | false |
| `tdm_measures_desc` | string | Description of TDM compliance measures | Auto-generated from scan |

---

## Section 3.2: Removal of Illegal Content

| Key | Type | Description | Default |
|-----|------|-------------|---------|
| `illegal_content_measures_desc` | string | Measures for illegal content removal | "TO BE PROVIDED" |

---

## Section 3.3: Other Information (Optional)

| Key | Type | Description | Default |
|-----|------|-------------|---------|
| `other_processing_info` | string | Additional processing information | "" |

---

## Usage Notes

1. **Tri-state fields**: All Yes/No questions in sections 2.1-2.6 use tri-state logic:
   - "Yes" - User explicitly confirmed
   - "No" - User explicitly denied
   - "TO_BE_PROVIDED" - Not yet specified by user

2. **Never auto-infer**: The tool will never automatically set Yes/No based on detected evidence. For example:
   - Finding domains does NOT auto-set `crawlers_used` to Yes
   - Finding public dataset matches does NOT auto-set `public_datasets_used` to Yes

3. **User overrides**: User-provided answers always take precedence over scan results

4. **Required fields**: Fields marked "TO BE PROVIDED" require user input before EU submission

5. **CSV generation**: The `crawled_domains_csv_path` is only populated if:
   - User explicitly sets `crawlers_used` to "Yes"
   - The CLI generates the top domains CSV file