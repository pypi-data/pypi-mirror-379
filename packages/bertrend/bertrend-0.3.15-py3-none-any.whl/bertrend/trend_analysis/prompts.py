#  Copyright (c) 2024, RTE (https://www.rte-france.com)
#  See AUTHORS.txt
#  SPDX-License-Identifier: MPL-2.0
#  This file is part of BERTrend.
import os
from datetime import datetime
from pathlib import Path

from jinja2 import Template, Environment, FileSystemLoader
from loguru import logger

from bertrend import OUTPUT_PATH
from bertrend.trend_analysis.data_structure import TopicSummaryList, SignalAnalysis

# Global variables for prompts
SIGNAL_INTRO = {
    "en": """As an elite strategic foresight analyst with extensive expertise across multiple domains and industries, your task is to conduct a comprehensive evaluation of a potential signal derived from the following topic summary:

{summary_from_first_prompt}

Leverage your knowledge and analytical skills to provide an in-depth analysis of this signal's potential impact and evolution:
""",
    "fr": """En tant qu'analyste de prospective stratégique d'élite avec une expertise étendue dans de multiples domaines et industries, votre tâche est de mener une évaluation complète d'un signal potentiel dérivé du résumé de sujet suivant :

{summary_from_first_prompt}

Utilisez vos connaissances et compétences analytiques pour fournir une analyse approfondie de l'impact potentiel et de l'évolution de ce signal :
""",
}

SIGNAL_INSTRUCTIONS = {
    "en": """
Analyze this signal only if the input data is sufficiently complete. If the subject summary lacks completeness, substance or novelty, respond with an empty JSON dictionary: {} 

For substantial signals, provide:

1. Potential Impact Analysis:
   - Examine the potential effects of this signal on various sectors, industries, and societal aspects.
   - Consider both short-term and long-term implications.
   - Analyze possible ripple effects and second-order consequences.

2. Evolution Scenarios:
   - Describe potential ways this signal could develop or manifest in the future.
   - Consider various factors that could influence its trajectory.
   - Explore both optimistic and pessimistic scenarios.

3. Interconnections and Synergies:
   - Identify how this signal might interact with other current trends or emerging phenomena.
   - Discuss potential synergies or conflicts with existing systems or paradigms.

4. Drivers and Inhibitors:
   - Analyze factors that could accelerate or amplify this signal.
   - Examine potential barriers or resistances that might hinder its development.

Your analysis should be thorough and nuanced, going beyond surface-level observations. Draw upon your expertise to provide insights that capture the complexity and potential significance of this signal. Don't hesitate to make well-reasoned predictions about its potential trajectory and impact.

Focus on providing a clear, insightful, and actionable analysis that can inform strategic decision-making and future planning.
If analysis cannot be substantiated with clear reasoning, omit that section.

=== OUTPUT QUALITY STANDARDS ===
Your analysis must avoid:

- **Vague Generalizations**: Broad, non-specific statements without concrete backing
- **Obvious Conclusions**: Widely known facts or predictable outcomes without new insights
- **Insufficient Evidence**: Claims lacking concrete examples, specific data points, or substantial proof
- **Generic Observations**: Analysis that could apply to any context without specificity
- **Circular Reasoning**: Implications that merely restate the original observation
- **Superficial Treatment**: Surface-level analysis without depth or nuance
- **Unsubstantiated Speculation**: Predictions or scenarios without logical foundation
- **Outdated Perspectives**: Analysis based on obsolete information or frameworks

=== MINIMUM QUALITY REQUIREMENTS ===
Each analysis section must demonstrate at least 2 of the following:

- **Specific Context**: Clear temporal, geographic, or sectoral boundaries and examples
- **Concrete Evidence**: Quantifiable insights, verifiable examples, or substantiated claims
- **Novel Perspectives**: Fresh angles, non-obvious connections, or emerging patterns
- **Actionable Intelligence**: Insights that enable informed decision-making or strategic planning
- **Cross-Domain Impact**: Implications across multiple sectors, industries, or domains
- **Measurable Dimensions**: Identifiable metrics, indicators, or tracking mechanisms
- **Causal Analysis**: Clear cause-and-effect relationships or contributing factor identification
- **Strategic Relevance**: Direct connection to business, policy, or societal decision-making

=== OUTPUT REQUIREMENTS ===
- **Quality Control**: Each section must meet the minimum standards above - omit any section that cannot achieve this threshold
- **Evidence-Based**: Use specific, quantifiable language with concrete examples and evidence
- **Confidence Levels**: Clearly distinguish between high-confidence assessments and speculative insights
- **Decision-Focused**: Prioritize actionable intelligence for strategic decision-makers
- **Balanced Objectivity**: Maintain analytical rigor while acknowledging uncertainties and limitations
- **Temporal Structure**: Organize insights across immediate (1-2 years), medium (3-5 years), and long-term (5-10 years) horizons
- **Omission Protocol**: If any analysis section cannot be substantiated with clear reasoning and evidence, omit it entirely rather than providing weak content

""",
    "fr": """
Analysez ce signal uniquement si les données d’entrée sont suffisamment complètes. Si le résumé du sujet manque d'éléments, de substance ou de nouveauté, répondez avec un dictionnaire JSON vide : {}

Pour les signaux substantiels, fournissez :

1. Analyse de l'Impact Potentiel :
   - Examinez les effets potentiels de ce signal sur divers secteurs, industries et aspects sociétaux.
   - Considérez les implications à court et à long terme.
   - Analysez les effets d'entraînement possibles et les conséquences de second ordre.

2. Scénarios d'Évolution :
   - Décrivez les façons potentielles dont ce signal pourrait se développer ou se manifester à l'avenir.
   - Considérez divers facteurs qui pourraient influencer sa trajectoire.
   - Explorez des scénarios optimistes et pessimistes.

3. Interconnexions et Synergies :
   - Identifiez comment ce signal pourrait interagir avec d'autres tendances actuelles ou phénomènes émergents.
   - Discutez des synergies ou conflits potentiels avec les systèmes ou paradigmes existants.

4. Moteurs et Inhibiteurs :
   - Analysez les facteurs qui pourraient accélérer ou amplifier ce signal.
   - Examinez les obstacles ou résistances potentiels qui pourraient entraver son développement.

Votre analyse doit être approfondie et nuancée, allant au-delà des observations superficielles. Appuyez-vous sur votre expertise pour fournir des insights qui capturent la complexité et l'importance potentielle de ce signal. N'hésitez pas à faire des prédictions bien raisonnées sur sa trajectoire et son impact potentiels.

Concentrez-vous sur la fourniture d'une analyse claire, perspicace et exploitable qui peut éclairer la prise de décision stratégique et la planification future.
Si l'analyse ne peut être étayée par un raisonnement clair, omettez cette section.

=== STANDARDS DE QUALITÉ DE SORTIE ===
Votre analyse doit éviter :

- **Généralisations Vagues** : Déclarations larges et non spécifiques sans fondement concret
- **Conclusions Évidentes** : Faits largement connus ou résultats prévisibles sans nouveaux insights
- **Preuves Insuffisantes** : Affirmations manquant d'exemples concrets, de données spécifiques, ou de preuves substantielles
- **Observations Génériques** : Analyse qui pourrait s'appliquer à n'importe quel contexte sans spécificité
- **Raisonnement Circulaire** : Implications qui ne font que reformuler l'observation originale
- **Traitement Superficiel** : Analyse de surface sans profondeur ni nuances
- **Spéculation Non Étayée** : Prédictions ou scénarios sans fondement logique
- **Perspectives Obsolètes** : Analyse basée sur des informations ou cadres dépassés

=== EXIGENCES MINIMALES DE QUALITÉ ===
Chaque section d'analyse doit démontrer au moins 2 des éléments suivants :

- **Contexte Spécifique** : Limites temporelles, géographiques, ou sectorielles claires avec exemples
- **Preuves Concrètes** : Insights quantifiables, exemples vérifiables, ou affirmations étayées
- **Perspectives Nouvelles** : Angles frais, connexions non évidentes, ou modèles émergents
- **Intelligence Actionnable** : Insights permettant une prise de décision éclairée ou une planification stratégique
- **Impact Trans-Domaine** : Implications sur plusieurs secteurs, industries, ou domaines
- **Dimensions Mesurables** : Métriques, indicateurs, ou mécanismes de suivi identifiables
- **Analyse Causale** : Relations de cause à effet claires ou identification de facteurs contributifs
- **Pertinence Stratégique** : Connexion directe avec la prise de décision business, politique, ou sociétale

=== EXIGENCES DE SORTIE ===
- **Contrôle Qualité** : Chaque section doit respecter les standards minimaux ci-dessus - omettez toute section qui ne peut atteindre ce seuil
- **Basé sur les Preuves** : Utilisez un langage spécifique et quantifiable avec des exemples concrets et des preuves
- **Niveaux de Confiance** : Distinguez clairement entre évaluations haute confiance et insights spéculatifs
- **Orienté Décision** : Priorisez l'intelligence actionnable pour les décideurs stratégiques
- **Objectivité Équilibrée** : Maintenez la rigueur analytique tout en reconnaissant les incertitudes et limitations
- **Structure Temporelle** : Organisez les insights sur les horizons immédiats (1-2 ans), moyens (3-5 ans), et long terme (5-10 ans)
- **Protocole d'Omission** : Si une section d'analyse ne peut être étayée par un raisonnement et des preuves clairs, omettez-la entièrement plutôt que de fournir un contenu faible

""",
}

TOPIC_SUMMARY_PROMPT = {
    "en": """
As an expert analyst specializing in trend analysis and strategic foresight, your task is to provide a comprehensive evolution summary of Topic {topic_number}. Use only the information provided below:

{content_summary}

Structure your analysis as follows:

For the first timestamp:

## [Concise yet impactful title capturing the essence of the topic at this point]
### Date: [Relevant date or time frame - format %Y-%m-%d]
### Key Developments
- [Bullet point summarizing a major development or trend]
- [Additional bullet points as needed]

### Analysis
[2-3 sentences maximum providing deeper insights into the developments, their potential implications, and their significance in the broader context of the topic's evolution]

For all subsequent timestamps:

## [Concise yet impactful title capturing the essence of the topic at this point]
### Date: [Relevant date or time frame - format %Y-%m-%d]
### Key Developments
- [Bullet point summarizing a major development or trend]
- [Additional bullet points as needed]

### Analysis
[2-3 sentences maximum providing deeper insights into the developments, their potential implications, and their significance in the broader context of the topic's evolution]

### What's New
[1-2 sentences maximum highlighting how this period differs from the previous one, focusing on new elements or significant changes]

Provide your analysis using only this format, based solely on the information given. Do not include any additional summary or overview sections beyond what is specified in this structure.
""",
    "fr": """
En tant qu'analyste expert spécialisé dans l'analyse des tendances et la prospective stratégique, votre tâche est de fournir un résumé complet de l'évolution du Sujet {topic_number}. Utilisez uniquement les informations fournies ci-dessous :

{content_summary}

Structurez votre analyse comme suit :

Pour le premier timestamp :

## [Titre concis mais percutant capturant l'essence du sujet à ce moment]
### Date : [Date ou période pertinente - format %Y-%m-%d]
### Développements Clés
- [Point résumant un développement majeur ou une tendance]
- [Points supplémentaires si nécessaire]

### Analyse
[2-3 phrases maximum fournissant des insights plus profonds sur les développements, leurs implications potentielles et leur importance dans le contexte plus large de l'évolution du sujet]

Pour tous les timestamps suivants :

## [Titre concis mais percutant capturant l'essence du sujet à ce moment]
### Date : [Date ou période pertinente - format %Y-%m-%d]
### Développements Clés
- [Point résumant un développement majeur ou une tendance]
- [Points supplémentaires si nécessaire]

### Analyse
[2-3 phrases maximum fournissant des insights plus profonds sur les développements, leurs implications potentielles et leur importance dans le contexte plus large de l'évolution du sujet]

### Nouveautés
[1-2 phrases maximum soulignant en quoi cette période diffère de la précédente, en se concentrant sur les nouveaux éléments ou les changements significatifs]

Fournissez votre analyse en utilisant uniquement ce format, basé uniquement sur les informations données. N'incluez pas de sections de résumé ou d'aperçu supplémentaires au-delà de ce qui est spécifié dans cette structure.
""",
}


def get_prompt(
    language: str,
    prompt_type: str,
    topic_number: int = None,
    content_summary: str = None,
    summary_from_first_prompt: str = None,
):
    lang = "en" if language == "English" else "fr"

    if prompt_type == "weak_signal":
        prompt = (
            SIGNAL_INTRO[lang].format(
                summary_from_first_prompt=summary_from_first_prompt
            )
            + SIGNAL_INSTRUCTIONS[lang]
        )

    elif prompt_type == "topic_summary":
        prompt = TOPIC_SUMMARY_PROMPT[lang].format(
            topic_number=topic_number, content_summary=content_summary
        )
    else:
        raise ValueError(f"Unsupported prompt type: {prompt_type}")

    return prompt


def save_html_output(html_output, output_file="signal_llm.html"):
    """Function to save the model's output as HTML"""
    output_path = OUTPUT_PATH / output_file

    # Save the cleaned HTML
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(html_output)
    logger.debug(f"Cleaned HTML output saved to {output_path}")


def fill_html_template(
    topic_summary_list: TopicSummaryList,
    signal_analysis: SignalAnalysis,
    language: str = "fr",
) -> str:
    """Fill the HTML template with appropriate data"""
    # Setup Jinja2 environment
    template_dir = os.path.dirname(os.path.abspath(__file__))
    env = Environment(
        loader=FileSystemLoader(template_dir),
    )
    template = env.get_template(
        "signal_llm_template_en.html"
        if language == "en"
        else "signal_llm_template_fr.html"
    )

    # Sort the list by date from most recent to least recent
    try:
        sorted_topic_summary_by_time_period = sorted(
            topic_summary_list.topic_summary_by_time_period,
            key=lambda x: datetime.strptime(x.date, "%Y-%m-%d"),
            reverse=True,
        )
        topic_summary_list.topic_summary_by_time_period = (
            sorted_topic_summary_by_time_period
        )
    except Exception as e:
        logger.warning("Cannot sort summaries by date, probably wrong date format")

    # Render the template with the provided data
    rendered_html = template.render(
        topic_summary_list=topic_summary_list, signal_analysis=signal_analysis
    )

    # FIXME: many \n are added...
    rendered_html = rendered_html.replace("\n", "")
    rendered_html = rendered_html.replace("\\'", "'")

    return rendered_html
