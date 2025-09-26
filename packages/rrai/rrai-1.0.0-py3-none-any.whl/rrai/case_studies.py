# case_studies.py
AMAZON_AI_HIRING_BIAS = """
Amazon’s AI Hiring Bias
Introduction
Artificial Intelligence (AI) has increasingly been integrated into human resources functions,
with promises to streamline recruitment and reduce human bias. However, as demonstrated
by the widely publicized case of Amazon’s experimental AI hiring tool, reliance on AI in
recruitment brings its own set of risks and challenges—most notably, the amplification of
existing biases. Amazon’s project, once seen as a +benchmark for AI-driven efficiency, ended
up serving as a cautionary tale for organizations aiming to leverage machine learning in
critical decision-making processes
.
Background
In the early-to-mid 2010s, Amazon sought to automate and optimize their high-volume
recruitment operations by developing a proprietary AI-powered hiring tool. The system was
trained on ten years of resumes submitted to Amazon, hoping to replicate the attributes of
successful past hires. This was part of a wider trend in the tech industry, where maledominated workforce histories disproportionately informed the composition of “ideal”
candidates
.
The tool scored job applications on a one to five star scale, intending to identify top talent
more objectively and efficiently than human recruiters could—reducing both workload and
subjective bias in screening candidates
.
Problem Statement
Despite its promising premise, Amazon’s AI hiring tool developed a significant gender bias,
systematically penalizing applications that contained words like “women’s” (e.g., “women’s
chess club captain”), and downgrading candidates from all-women’s colleges[2][6][4]. The root
of the problem lay in the algorithm’s training data—reflecting a workforce and application
pool dominated by men—which led the AI to associate male characteristics and histories with
job success, while undervaluing or ignoring female candidates
.
The main issues were:
• Discrimination against female applicants for technical roles.
• Reinforcement and amplification of historical gender imbalances in tech hiring.
• Difficulty in remediating embedded bias after deployment
.
Methodology
Amazon’s machine learning specialists developed the tool using supervised learning
techniques on historical hiring data. The system ingested resumes and results of previous

hiring decisions, seeking to uncover patterns correlated with “successful” employees.
However, because the historical data was skewed—most hires were men, reflecting broader
tech industry trends—the model learned to favor resumes that mirrored past hires (i.e., men)
and penalized those that did not (i.e., women)[6][5][4]
.
Efforts to fix the tool’s gender bias included:
• Editing the algorithms to ignore explicit gendered keywords like “women’s,”
• Trying to neutralize the impact of potentially biased features,
• Testing outputs for unintended discriminatory patterns
.
However, these corrections proved insufficient, as the tool persisted in finding proxies for
gender discrimination
.
Presentation
The practical effect was that the tool would consistently score resumes from male candidates
higher than similarly qualified female candidates. This was not due to an explicit directive, but
rather the machine learning model’s reliance on patterns from a male-majority dataset

Even after removing gendered words from consideration, the system “learned” other ways of
downgrading female candidates, such as penalizing certain schools or extracurricular
activities linked with women
.
Amazon’s official position was that this AI tool was never used as the sole factor in hiring
decisions; instead, human recruiters reviewed its rankings alongside other information[1][6]
.
Nonetheless, persistent issues and inability to guarantee bias-free operation led Amazon to
scrap the project entirely in 2018
.
Discussion
This case illustrates several important lessons about the limitations of AI in decision-making:
• Algorithmic bias is an amplification of societal and historical human biases: Even
with the best intentions, algorithms trained on skewed data will reproduce (and scale)
those biases, particularly in sensitive domains like hiring[2][4]
.
• Transparency and auditability are critical: Proprietary, black-box algorithms make it
difficult to investigate or understand why biased decisions are being made, limiting both
trust and accountability
.
• Technical fixes alone are rarely enough: Invalidating some biased features only
pushed the AI to find others, highlighting that remediation after deployment is extremely
difficult without rethinking data collection and training frameworks
.
• Human oversight and ethical vigilance are required: Technology should augment,
not fully replace, human judgment. Continual monitoring and periodic auditing of AI
outputs are essential to catch ingrained or emergent bias
.
Conclusion

Amazon’s failed experiment with AI-assisted hiring underscores the complexity of
algorithmic fairness and the dangers of unchecked automation in HR. The project’s
abandonment sent a strong message to other organizations: diverse and representative
data, ongoing oversight, and robust ethical frameworks are not optional, but
foundational to trustworthy AI deployment in human resources[3][11][4]. While AI offers
scalability and speed, it cannot be assumed to be inherently fair—without careful design and
constant review, it risks compounding inequities rather than solving them.
"""

APPLE_CARD_GENDER_BIAS = """
Apple Card Gender Bias Controversy
Introduction
The Apple Card gender bias controversy highlighted significant concerns about fairness and
discrimination in algorithmic decision-making within financial services. Launched in 2019 by Apple
in partnership with Goldman Sachs, the Apple Card used an automated system to determine credit
limits for applicants. Soon after launch, allegations surfaced that the algorithm systematically
assigned lower credit limits to women compared to men, even when they shared similar financial
profiles. This case brought to light the complex challenges of ensuring fairness in AI-driven
financial products and raised important questions about transparency, regulatory oversight, and the
ethical use of automated decision tools.
Background
Apple Card was introduced as a new kind of credit card that integrates seamlessly with Apple’s
ecosystem and offers a user-friendly interface, no fees, and rewards. Goldman Sachs, as the issuing
bank, employed an algorithmic underwriting process to evaluate applicants’ creditworthiness and
assign credit limits.
Soon after launch, customers and industry observers began reporting cases where women applicants
received credit limits significantly lower than those of their male partners or spouses, despite
comparable or better financial standing. High-profile media coverage and social media amplification
prompted widespread scrutiny of Goldman Sachs’ credit evaluation algorithms.
The controversy took on broader importance given the traditional challenges women face in
accessing fair credit and the increasing reliance on AI and machine learning systems in financial
services.
Problem Statement
The core problem was the apparent gender bias exhibited by the Apple Card’s credit limit
algorithm:
• Women were systematically assigned lower credit limits compared to men with similar
financial qualifications.
• The algorithm reportedly failed to adequately consider or neutralize gender as a factor
influencing credit decisions.
• The opaque, proprietary nature of Goldman Sachs' credit scoring and underwriting process left
consumers and regulators unable to fully evaluate or challenge the decision logic.
• Allegations suggested that the system could be perpetuating gender-based financial
discrimination, which is illegal under US Equal Credit Opportunity laws.
This raised urgent questions regarding fairness, algorithm transparency, accountability, and the
intersection of automated systems with anti-discrimination regulations.

Methodology
Goldman Sachs reportedly used machine learning and traditional credit scoring models to evaluate
creditworthiness for Apple Card applicants. While exact methodological details have not been
publicly disclosed, the process likely involved:
• Data inputs: Applicant credit reports, income, debt levels, credit utilization, payment history,
and other financial metrics.
• Algorithm training: Utilizing historical credit data and traditional credit scoring models. The
system aimed to predict credit risk and set appropriate credit limits accordingly.
• Automated decision-making: The algorithm produced credit limit decisions without explicit
human override unless applicants requested reconsideration.
• Evaluation and continuous learning: The system purportedly incorporated ongoing data to
refine its assessments, though details on bias detection or mitigation were not publicly detailed.
Following the controversy, Goldman Sachs announced an internal review of credit decisions in
response to the allegations and external inquiries.
Presentation
Empirical observations and anecdotal evidence presented the following patterns:
• Women applicants reported credit limits 5 to 10 times lower than their male spouses despite
shared finances and excellent credit.
• Skeptics noted that some men could receive significantly higher limits solely by virtue of their
gender or other correlated factors.
• The disparity became widely publicized on social media and in news outlets, prompting
consumer complaints and regulatory interest.
• Goldman Sachs denied that the algorithm discriminated based on gender, asserting that credit
decisions were consistent with regulatory standards and based solely on creditworthiness.
• Despite those denials, the lack of transparency in the model’s decision logic left customers and
third-party experts unable to validate the fairness of the process independently.
Apple and Goldman Sachs both faced reputational risks amid calls for greater transparency and
accountability.
Discussion
This case emphasizes critical facets of algorithmic bias and financial fairness:
• Algorithmic bias can arise through correlated variables: Even if gender is not explicitly
used, proxies like income type, employment sector, or credit history nuances can lead to biased
outcomes.
• Transparency matters for trust and accountability: Proprietary financial algorithms often
operate as “black boxes,” making it difficult for consumers and regulators to identify and
correct unfair discrimination.

• Legal and ethical compliance is mandatory: Financial services must comply with antidiscrimination laws such as the Equal Credit Opportunity Act (ECOA) in the US. Automated
systems require careful auditing to ensure adherence.
• Bias mitigation requires proactive monitoring and intervention: Regular audits, bias
testing, and diverse training data can help reduce discriminatory effects.
• Human oversight remains important: Automated credit decisions should be reviewed and
appealable to prevent unjust denials or unfair treatment.
• Public scrutiny and regulatory pressure foster improvements: These controversies push
institutions to enhance fairness and accountability in algorithmic decision-making.
Conclusion
The Apple Card gender bias controversy highlights the challenges of relying on automated credit
evaluation systems in sensitive financial domains. It shows that:
• Algorithmic decision-making, while efficient, is vulnerable to perpetuating systemic biases
embedded in training data.
• Transparency, rigorous testing, and legal compliance are essential to protect consumers from
unfair discrimination.
• Financial institutions must establish robust mechanisms for bias detection, remediation, and
recourse to maintain public trust and uphold ethical standards.
• The case serves as a cautionary tale that innovation in fintech requires not only technical
sophistication but also strong commitments to fairness, transparency, and regulatory
compliance.
"""

GOOGLE_PHOTOS_TAGGING = """
Google Photos Tagging Incident
Introduction
With the increasing adoption of artificial intelligence (AI) in consumer technology, image
recognition and automatic tagging have become prominent features in many applications. Google
Photos, a popular photo storage and organization platform, utilized advanced AI algorithms to
automatically recognize and categorize images, enhancing user experience. However, in 2015,
Google Photos faced a major controversy when its automatic tagging system mistakenly labeled
photographs of African American individuals as "gorillas." This incident exposed critical issues
surrounding algorithmic bias, the limitations of AI image recognition, and the social implications of
automated technology errors, prompting a reevaluation of AI training data, fairness, and
accountability.
Background
Google Photos was launched in May 2015 as part of Google’s suite of cloud services. It leveraged
state-of-the-art machine learning techniques, particularly convolutional neural networks, to analyze
and classify images based on their visual content. The automatic tagging feature aimed to help users
organize and search photos quickly by recognizing faces, objects, and scenes.
In July 2015, users began reporting that the AI system was incorrectly tagging pictures of Black
people as "gorillas," a highly offensive and racially insensitive error. This occurrence rapidly
gathered media attention, raising discussions about bias in AI and the consequences of training
machine learning models on insufficiently diverse datasets. Google swiftly apologized and removed
the "gorilla" label from the system, but the incident left a lasting impact on both the public’s
perception of AI fairness and the industry’s approach to ethical AI development.
Problem Statement
The central problem in the Google Photos tagging incident involved:
• The racial bias embedded in the image recognition algorithm that led to African American
faces being mislabeled as "gorillas."
• Insufficient training data diversity, causing the AI to misidentify darker-skinned individuals
due to underrepresentation or poor-quality samples in the training sets.
• Algorithmic insensitivity to the cultural offensiveness and historical context of certain labels,
resulting in social harm.
• Lack of adequate testing and validation mechanisms for edge cases involving racial or
ethnic minorities before deployment.
• The potential erosion of user trust in AI technologies due to such high-profile errors.
These challenges highlight broader issues in AI ethics related to fairness, data quality, and cultural
awareness.

Methodology
Google Photos’ image tagging algorithm operated using machine learning techniques:
• Training Data: The AI was trained on vast datasets containing millions of images labeled
with various tags. However, the composition and diversity of these datasets were insufficient
to correctly classify all racial groups.
• Model Architecture: A deep learning model, likely a convolutional neural network, learned
to identify patterns such as facial features, textures, and shapes to label images.
• Label Assignment: The algorithm assigned predefined tags based on the model’s confidence
scores.
• Evaluation: Prior to release, the system’s accuracy was tested on benchmark datasets, though
these tests apparently lacked rigorous checks against racial bias or sensitive categories.
• Post-incident response: Following the controversy, Google removed the "gorilla" label and
later implemented measures to disable or modify certain problematic tags.
Despite these actions, the incident demonstrated the complexity of fully training AI systems to
handle sensitive categories accurately.
Presentation
The incident manifested as follows:
• Users uploading photographs of Black friends or family members found these images
automatically grouped with or labeled as "gorillas."
• Public and media outcry ensued, criticizing Google for racial insensitivity and inadequate AI
oversight.
• Google issued a public apology, acknowledging the harm and promising improvements.
• The "gorilla" tag was removed from Google Photos, along with related tags such as
"chimpanzee" and "monkey," to prevent recurrence.
• The error was widely discussed as a vivid example of algorithmic bias affecting real users.
In subsequent software updates, Google reportedly enhanced its training datasets and tagging
protocols to reduce similar mistakes.
Discussion
The Google Photos tagging incident presents several important lessons:
• Training Data Diversity is Essential: AI systems require inclusive, representative datasets to
perform accurately across different demographic groups. Underrepresentation can lead to
systematic misclassifications.
• Algorithmic Bias Reflects Societal Biases: AI inherits biases present in its training data,
confronting developers with complex challenges to identify and correct harmful patterns.

• Cultural Sensitivity and Context Matter: Automated labeling must account for social and
historical contexts, especially when labels can cause offense or reinforce stereotypes.
• Limitations of Machine Learning Explainability: Understanding why the algorithm made
such errors remains difficult, necessitating transparency and interpretability efforts.
• Importance of Robust Testing and Human Oversight: Testing across diverse scenarios,
including edge cases, alongside human review is critical before rolling out AI features.
• Public Relations and Accountability: Prompt acknowledgment and corrective action are
vital to restore user trust and demonstrate corporate responsibility.
This case served as a watershed moment in discussions about ethical AI deployment and the social
implications of machine learning.
Conclusion
The Google Photos racial tagging error underscores the profound challenges of deploying AI
systems in socially sensitive domains. It reveals that:
• Despite technical prowess, AI systems can perpetuate or magnify harmful biases if not
carefully designed and audited.
• Ensuring fairness and preventing discrimination requires deliberate attention to data quality,
cultural context, and ethical implications.
• Ongoing monitoring, transparency, and inclusivity must be integral to AI development
processes.
• This incident catalyzed broader awareness and action within the AI community to develop
more equitable technologies.
Ultimately, the case highlights that trustworthy AI depends not only on algorithms but also on
responsible stewardship by organizations deploying these technologies.
"""

HEALTHCARE_ALGORITHM_BIAS = """
Healthcare Algorithm Racial Bias
Introduction
The use of algorithms and artificial intelligence (AI) in healthcare has escalated rapidly, promising
improved efficiency and more objective patient assessment. However, significant evidence has
emerged that these systems can perpetuate or even amplify existing racial disparities if not carefully
designed and evaluated. A widely cited case involves a risk-prediction algorithm used by major U.S.
healthcare systems, which exhibited striking racial bias by underestimating the health needs of Black
patients. This incident has become a central example in the discussion of algorithmic fairness in
healthcare.
Background
Healthcare providers and insurers increasingly rely on AI-powered algorithms for tasks such as
predicting patient risk, allocating resources, and managing chronic diseases. One notable system
analyzed in recent studies was used to flag patients for special healthcare programs targeting those
with complex medical needs. The algorithm, developed by a commercial vendor, enrolled millions
of patients and influenced critical care management decisions for vulnerable populations.
In 2019, researchers analyzed one such algorithm in use by large U.S. healthcare organizations,
revealing systematic racial bias in how patient risk and needs were evaluated[1][2][3]
.
Problem Statement
The main problem identified was that Black patients received lower risk scores than equally sick
White patients when analyzed by the algorithm. The algorithm incorrectly assumed that lower
healthcare spending corresponded with better health, using costs as a proxy for medical complexity
and need. Due to structural inequalities, less money is historically spent on Black patients than White
patients with comparable health burdens, leading the algorithm to incorrectly deem Black patients
as healthier than they actually were[1][2][3]
.
The consequences included:
• Fewer Black patients identified for additional care programs.
• Reduced access to resources for already underserved communities.
• Heightened risk of poorer outcomes due to under-recognition of medical needs.
Methodology
The risk stratification algorithm operated by:
• Collecting health insurance claims data (such as past hospitalizations, prescriptions, medical
costs).
• Using historical healthcare spending as the main proxy for health status and risk.

• Assigning patients a risk score that guided enrollment into high-need care management
programs.
Researchers reviewed the medical records, diagnoses, and algorithmic scores of nearly 50,000
patients — over 6,000 of whom were Black — and compared actual health needs against algorithmdriven risk categorization[2][1]
.
When the algorithm categorized patients as "high-risk," 26% more chronic illnesses were found
among Black patients versus White ones at the same risk level.
Presentation
The bias manifested in health systems as:
• Dramatically lower rates of Black patients being referred to care management for similar
medical complexity.
• The percentage of Black patients receiving supplemental care through the program was only
17.7%. When race bias was corrected for, this rose to 46.5%[4]
.
• The root cause: reliance on healthcare costs — not on factors such as disease burden or direct
clinical indicators — as the principal predictor of patient needs[1][5][3]
.
Researchers developed and tested improved versions of the algorithm that used direct clinical
indicators, not cost, as the key factor. This change essentially eliminated the observed racial bias in
referrals.
Discussion
This case offers important insights:
• Proxy Measures Invite Bias: When algorithms use indirect measures (e.g., costs) as proxies
for needs, they risk embedding and perpetuating systemic inequalities[1][2][5]
.
• Data Diversity and Context Matter: Historical and structural racism in healthcare delivery
means past utilization/costs cannot be assumed to be neutral.
• Algorithmic Transparency and Oversight are Critical: Opaque algorithms make it difficult
to detect where and how bias is introduced. Open evaluation and regular auditing are
necessary[6][7]
.
• Stakeholder Engagement Is Key: Organizations and policymakers must include diverse
voices, especially those from affected communities, when designing and deploying healthcare
algorithms[7][6]
.
• Systemic Solutions Required: Technical fixes must be paired with broader reforms to address
underlying inequities in healthcare access and delivery[5][8]
.
Conclusion
The racial bias discovered in widely used healthcare algorithms is a stark warning that AI and big
data tools, if not designed and monitored carefully, can perpetuate or worsen inequities in health
outcomes. Algorithms should not rely on cost proxies alone, but should use direct, clinically relevant

predictors to ensure fair treatment and access. Transparency, diverse data, and multidisciplinary
oversight are crucial for trust and health equity.
Addressing these biases is not only a technical challenge but also a moral imperative for the
healthcare industry and for society as a whole.
"""

AI_DEEPFAKE_SCAMS = """
AI-Powered Deepfake Scams
Introduction
The rapid evolution of artificial intelligence (AI) has given rise to new forms of cybercrime, with
deepfake technology standing out as a particularly dangerous threat. Deepfakes use AI-driven audio,
video, or image manipulation to convincingly imitate real people, often for malicious purposes. This
case study examines high-profile AI-powered deepfake scams, analyzes their impacts, and offers
insights into mitigation strategies.
Background
Deepfake technology leverages machine learning algorithms—especially deep neural networks—to
synthesize lifelike audio and visual representations of individuals[1][2]. What started as a
technological curiosity is now a potent tool for fraudsters. Incidents of deepfake-enabled scams,
particularly in the financial sector, have skyrocketed, resulting in losses exceeding $200 million in
Q1 2025 alone[3][4]
.
Noteworthy cases include:
• A British engineering firm losing over $25 million to a deepfake CFO during a fraudulent
video conference[5][6]
.
• Scams targeting individuals and businesses using synthesized voices or videos of CEOs,
celebrities, and even close family members to request urgent transfers or promote bogus
investments[7][8]
.
Problem Statement
AI-powered deepfake scams present a formidable challenge by:
• Bypassing traditional security and trust mechanisms.
• Creating convincing digital impersonations to exploit human and organizational
vulnerabilities.
• Scaling attacks easily and cheaply across multiple victims and platforms[2][9]
.
Organizations and individuals face severe financial, reputational, and psychological risks.
Traditional defenses rooted in human intuition and visual verification are becoming obsolete due to
the realism and accessibility of deepfake technology.
Methodology
This case study draws on documented incidents, expert commentary, and industry whitepapers to
analyze:
• The tactics and technologies used in deepfake scams.

• Real-world events in corporate and individual settings.
• Strategies for detection, prevention, and response.
Data sources include published news articles, industry research, technical analyses, and regulatory
advisories[1][5][6][3][10]
.
Presentation: Deepfake Scam Incident
Incident Overview
In early 2024, a British engineering firm was the target of a sophisticated deepfake scam:
• Fraudsters used AI to create deepfake video and audio of the company’s CFO and other senior
staff.
• The deceived employee participated in a video call where deepfake avatars issued urgent
transfer instructions.
• The employee then transferred HK $200M (nearly USD $26M) into accounts controlled by
the scammers[1][5][6]
.
• By the time the deception was uncovered, the funds had disappeared into global bank accounts
beyond recovery.
Modus Operandi
• Voice and video cloning: Attackers replicate key individuals’ voices and appearances.
• Social engineering: Use of authority and urgency to override standard verification processes.
• Multi-channel attack: Video calls, emails, and messages reinforce the scam’s legitimacy.
Other Notable Cases
• Elon Musk deepfake videos promoting fraudulent investments[5][11]
.
• Celebrity and political impersonations used for scams and misinformation campaigns[7][11]
.
• Personal scams, such as the use of a deepfaked loved one’s voice to request emergency
funds[7]
.
Discussion
Deepfakes are making scams more personalized, persuasive, and scalable:
• Realism: AI-generated content can now fool even savvy, trained employees.
• Accessibility: Cloud platforms and off-the-shelf software democratize the creation of
deepfakes, lowering the barrier to crime[2][10]
.
• Scalability: Attackers can simultaneously target dozens or hundreds of victims using
automated tools[2][9][10]
.

• Social Impact: Beyond financial loss, victims face psychological distress, damage to
reputation, and erosion of public trust[3][7][12]
.
Industries most at risk include finance, government, legal, and education, but private citizens are
increasingly targeted. Non-financial scams, such as explicit synthetic media or misinformation in
politics, also pose rising threats[3][11][12]
.
Conclusion
Deepfake technology, powered by AI, has transformed the landscape of cyber-enabled fraud. The
number and sophistication of deepfake scams have sharply increased, causing unprecedented
financial and psychological harm. Traditional verification methods are now insufficient.
Mitigation strategies must include:
• Employee education and awareness.
• Implementation of advanced "liveness" and multi-factor verification systems.
• Ongoing monitoring of AI-generated content and rapid-response procedures to suspected
deepfake activity[5][2][9]
.
Organizations and the public must remain vigilant, adapt security protocols, and foster international
cooperation to counteract these evolving threats.
"""

CHATGPT_HALLUCINATIONS = """
Case Study No- 10
ChatGPT Hallucinations and False Information
Introduction
ChatGPT, developed by OpenAI, is among the most advanced large language models (LLMs) used
for conversational AI. Despite its impressive ability to generate human-like responses, a persistent
and significant problem is its tendency to produce “hallucinations” — confident outputs that are
factually incorrect, fabricated, or misleading. This issue not only impacts user trust but also raises
ethical, legal, and practical concerns[1][2][3]
.
Background
ChatGPT and similar LLMs are trained on vast datasets from the internet and other sources to predict
the next word in sequences, simulating conversation or generating coherent texts. However, the
underlying architecture does not “understand” information as humans do; it merely generates
plausible-sounding language from probability distributions learned during training. This results in
occasional hallucinations, particularly when responding to novel queries or domains outside its
training data[4][5][3]
.
Hallucinations in AI became particularly evident with ChatGPT’s widespread public deployment.
Studies and real-world cases have reported that the platform can generate non-existent sources, false
personal information, erroneous legal precedents, and fabricated scientific references, often with
remarkable confidence and fluency[6][2][7][8]
.
Problem Statement
Despite advancements in AI capabilities, ChatGPT frequently generates hallucinated content—
untrue or misleading information confidently presented as fact. These errors have implications for
legal, academic, medical, and personal contexts, where reliability and accuracy are paramount. The
inability to reliably detect or prevent these hallucinations limits the safe deployment of ChatGPT in
high-stakes domains[1][4][7][5]
.
Methodology
This case study combines:
• Review of scientific literature and articles on ChatGPT hallucinations.
• Analysis of real-world incidents and experimental findings regarding AI-generated falsehoods.
• Examination of technical documentation from OpenAI regarding the mechanisms of
hallucination and attempted mitigation strategies.
• Synthesis of methodologies used to benchmark hallucination rates, such as OpenAI's use of
datasets like PersonQA to evaluate the factual accuracy of model outputs[9]
.
Presentation

Definition of Hallucination
• AI hallucination refers to the generation of plausible but factually incorrect outputs by AI
systems like ChatGPT[2][3]
.
• These can range from fabricated statistics to entirely invented sources, quotes, or case law.
Real-world Examples
• In May 2023, a lawyer submitted a legal brief containing multiple fabricated case citations
generated by ChatGPT, which resulted in professional sanctions and sparked wide discussion
on the reliability of AI-generated legal content[6][8]
.
• ChatGPT has also been known to create fake personal information, such as non-existent birth
dates for public figures[7]
.
• Experiments have found a high proportion of errors in references and citations produced by
ChatGPT—one study found that only 7% of its produced references were both correct and
accurate[2][10][11]
.
• ChatGPT has fabricated negative personal claims, such as falsely accusing a professor of
misconduct and attributing the information to fictitious news articles[8]
.
• In customer service, ChatGPT hallucinated Air Canada’s refund policy, which led a user to an
incorrect, costly purchase decision[8]
.
Quantitative Data
• Studies find hallucination rates varying based on domain and prompt structure: one OpenAI
benchmark showed the o3 model hallucinated in 33% of factual queries, with the o4-mini
model reaching 48%[9]
.
• Reference accuracy studies indicate that 47% of ChatGPT references were fabricated and
another 46%, although referring to real materials, cited incorrect details[2][10]
.
Discussion
Causes
• Nature of LLMs: These models do not fact-check; they predict plausible text based on
patterns, not verifiable truth[2][3]
.
• Training Data Gaps: Models may “fill in the blanks” when lacking specific data, especially
for recent events or narrow topics[1][4][12]
.
• Prompt Design: Vague or biased prompts can lead to hallucinated outputs[8][11]
.
• Overreliance by Users: The fluent confidence of ChatGPT’s output may cause users to
mistake hallucinations for factual statements, leading to overreliance[5]
.
Detection & Mitigation
• Fact-checking: Manual verification remains essential, especially in high-risk contexts[13][12]
.

• Technical Approaches: OpenAI and others are researching anomaly detection, improved
datasets, prompt engineering, and retrieval-augmented generation to reduce
hallucinations[1][4][14]
.
• Human Oversight: Legal mandates (e.g., in EU law) require accurate, transparent
information, which current systems cannot always guarantee[7]
.
Ethical and Legal Implications
• Data Protection: Hallucinated personal information poses risks under regulations like
GDPR[7]
.
• Academic Integrity: Fabricated citations and evidence threaten the validity of scholarly
work[4][11]
.
• Professional Use: Misuse in law and medicine demonstrates potential for real-world harm[6][8]
.
Conclusion
ChatGPT’s hallucination problem underscores a fundamental limitation of current LLMs: they
generate plausible language but cannot guarantee factual accuracy. This challenge is both technical
and social, requiring ongoing research, user education, regulatory clarity, and complementary factchecking tools. Until robust solutions exist, users must remain vigilant and skeptical about
unverified claims, particularly in high-stakes scenarios[1][2][7][8][10][3]
"""

def get_case_study(name):
    lookup = {
        'amazon_ai_hiring_bias': AMAZON_AI_HIRING_BIAS,
        'apple_card_gender_bias': APPLE_CARD_GENDER_BIAS,
        'google_photos_tagging': GOOGLE_PHOTOS_TAGGING,
        'healthcare_algorithm_bias': HEALTHCARE_ALGORITHM_BIAS,
        'ai_deepfake_scams': AI_DEEPFAKE_SCAMS,
        'chatgpt_hallucinations': CHATGPT_HALLUCINATIONS
    }
    return lookup.get(name.lower(), "Case study not found.")

def print_case_study(name):
    print(get_case_study(name))

def get_all_case_studies():
    return {
        'amazon_ai_hiring_bias': AMAZON_AI_HIRING_BIAS,
        'apple_card_gender_bias': APPLE_CARD_GENDER_BIAS,
        'google_photos_tagging': GOOGLE_PHOTOS_TAGGING,
        'healthcare_algorithm_bias': HEALTHCARE_ALGORITHM_BIAS,
        'ai_deepfake_scams': AI_DEEPFAKE_SCAMS,
        'chatgpt_hallucinations': CHATGPT_HALLUCINATIONS
    }
