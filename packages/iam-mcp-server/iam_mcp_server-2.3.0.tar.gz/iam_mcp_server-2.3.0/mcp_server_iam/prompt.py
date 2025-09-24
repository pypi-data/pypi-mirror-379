from datetime import datetime
from functools import lru_cache
from typing import Annotated, Literal

from pydantic import Field


async def analyze_job_market(
    role: Annotated[
        str,
        Field(description="Job role/title to analyze market trends for", min_length=1),
    ],
    city: Annotated[
        str | None,
        Field(description="Target city for market analysis (requires country)"),
    ] = None,
    country: Annotated[
        str | None, Field(description="Target country for market analysis")
    ] = None,
    platform: Annotated[
        Literal["linkedin", "indeed", "glassdoor", ""] | None,
        Field(description="Specific platform to focus analysis on"),
    ] = None,
    num_jobs: Annotated[
        int,
        Field(
            description="Number of job listings to analyze for market trends",
            default=5,
            ge=1,
            le=20,
        ),
    ] = 5,
) -> str:
    """
    Generate comprehensive job market analysis prompt for specified role and location.

    Args:
        role: Job role/title to analyze market trends for
        city: Target city for market analysis (requires country)
        country: Target country for market analysis
        platform: Specific platform to focus analysis on
        num_jobs: Number of job listings to analyze for market trends (1-20, default 5)

    Returns:
        str: A structured prompt that guides LLM to analyze job market trends, salary
        ranges, skill requirements, and employment patterns for the specified position.
    """

    return f"""
    # System / Instruction Prompt for LLM
    You are a data-driven AI assistant, your task is to analyze the job market for the top {num_jobs} positions matching a given {role}, optionally filtered by {city} and {country}, and sourced from {platform}.
    Before you run any tools or compose your final output, **outline your high-level approach** in 3–5 bullet points, showing that you’ve thought through every step.

    ## Task Definition
    Analyze the job market for:
    - **Role:** `{role}`
    - **Location:**  
    - City: `{city}` (optional)  
    - Country: `{country}` (required if city is given)  
    - **Platform:** `{platform}` (must be one of `linkedin`, `indeed`, `glassdoor`, or empty)

    ## Pre-Execution Checklist
    1. **Validate inputs**  
    - If `city` is non-empty, ensure `country` is also provided.  
    - If `platform` is non-empty, ensure it is one of `linkedin`, `indeed`, or `glassdoor`.  
    2. **Plan your analysis**  
    - Decide which fields to extract (`title`, `company`, `type`, `description`, `salary`, `work_arrangement`).  
    - Determine how you’ll aggregate and summarize skills/keywords and salary data.  

    ## Execution Steps
    1. **Invoke MCP tool**  
    - run `search_jobs` mcp tool with suitable roles, city, country, platform and num_jobs.
    2. **Extract & Review**  
    - Pull out `title`, `company`, `type` (e.g., Full-time/Contract), `description`, `salary` (if present), `remote/onsite`.  
    3. **Aggregate Insights**  
    - **Top roles:** List and count unique job titles.  
    - **Key skills & keywords:** Identify the most frequent.  
    - **Salary trends:** Compute average, median, range.  
    - **Work arrangement:** Tally remote vs. onsite vs. hybrid.  
    4. **Draft Markdown Report**  
    - Use headings (`## Most Common Roles`, `## Skills & Keywords`, etc.).  
    - Present tables or bullet lists for clarity.  
    - Conclude with a brief summary highlighting any surprises or actionable takeaways.

    ## Output
    Produce a markdown-formatted report under these sections:
    1. **Approach Overview** (your pre-execution bullets)  
    2. **Data Summary**  
    3. **Insights & Trends**  
    4. **Recommendations** (optional: e.g., “Consider upskilling in X…”)

    Thank you for your meticulous analysis.  
    """


def save_jobs(
    jobs_dir: Annotated[str, Field(description="Directory to save jobs")],
    date: Annotated[str, Field(description="Date of the job search")],
    role: Annotated[str, Field(description="Role of the job search")],
    city: Annotated[
        str | None,
        Field(description="Target city for job search"),
    ] = None,
    country: Annotated[
        str | None, Field(description="Target country for market analysis")
    ] = None,
    num_jobs: Annotated[
        int,
        Field(description="Number of jobs to save", default=5, ge=1, le=100),
    ] = 5,
) -> str:
    """
    Generate instructions for saving job search results to a JSON file.

    Creates detailed LLM instructions for properly formatting and saving
    job data as a structured JSON file with consistent naming conventions.

    Args:
        jobs_dir: Target directory path for saving the job file
        date: Date when the job search was performed (YYYY-MM-DD format)
        role: Job role/title that was searched for
        num_jobs: Number of job results to save (1-100, default 5)
        city: City/location that was searched in
        country: Country/location that was searched in

    Returns:
        str: Formatted prompt with detailed instructions for the LLM to save
        job data as a properly structured JSON file.
    """
    # Sanitize inputs for safe filename generation
    safe_role = "".join(c for c in role if c.isalnum() or c in (" ", "-", "_")).strip()
    safe_role = safe_role.replace(" ", "_")

    # Build filename parts dynamically based on what's provided
    filename_parts = [date, safe_role]

    if city:
        safe_city = "".join(
            c for c in city if c.isalnum() or c in (" ", "-", "_")
        ).strip()
        safe_city = safe_city.replace(" ", "_")
        filename_parts.append(safe_city)

    if country:
        safe_country = "".join(
            c for c in country if c.isalnum() or c in (" ", "-", "_")
        ).strip()
        safe_country = safe_country.replace(" ", "_")
        filename_parts.append(safe_country)

    filename_parts.append(str(num_jobs))
    filename = "_".join(filename_parts) + ".json"

    return f"""
# System Instructions for Saving Job Search Results

You are tasked with saving job search results to a structured JSON file. Follow these instructions precisely:

## File Location and Naming
- **Directory**: Save to `{jobs_dir}` directory
- **Filename**: `{filename}`
- **Format**: JSON array containing job objects

## Required JSON Structure
Each job must be saved with this exact structure:

```json
[
  {{
    "job_id": "string - unique identifier for the job",
    "title": "string - job title/position name", 
    "company": "string - employer/company name",
    "city": "string - job location city",
    "country": "string - job location country",
    "description": "string - job description or summary",
    "apply_link": "string - application URL or 'Not provided'",
    "saved_date": "{date}",
    "search_criteria": {{
      "role": "{role}",
      "city": "{city}",
      "country": "{country}",
      "date_searched": "{date}"
    }}
  }}
]
```

## Critical Instructions

1. **Create the directory** `{jobs_dir}` if it doesn't exist
2. **Use the EXACT filename format**: `{filename}`
3. **Ensure valid JSON**: 
   - Proper escaping of quotes and special characters
   - No trailing commas
   - Proper array structure with square brackets
4. **Handle missing data**: Use `null` for missing fields, never leave undefined
5. **Preserve data integrity**: Don't modify or truncate important information
6. **Add metadata**: Include search criteria and save date for tracking

## Data Validation
- Verify all job objects have the required fields
- Ensure `apply_link` is a valid URL or "Not provided"
- Check that `job_id` is unique within the array
- Validate that the JSON is properly formatted before saving

## Success Confirmation
After saving, confirm:
- File was created at the correct path
- JSON is valid and parseable  
- All {num_jobs} jobs were saved successfully
- File size is reasonable (not empty or corrupted)

## IMPORTANT
- Use the `write_file` tool to write the JSON file with the exact filename and structure specified above.
"""


def mesh_resumes(
    save_directory: Annotated[
        str,
        Field(
            description="Directory to save the resume mesh",
            min_length=1,
        ),
    ],
    resume_mesh_filename: Annotated[
        str,
        Field(
            description="Filename for the resume mesh", pattern=r"^[a-zA-Z0-9_\-]+\.md$"
        ),
    ],
    date: Annotated[str, Field(description="Date of the job search")],
) -> str:
    """
    Generate a resume mesh prompt for merging multiple resumes.

    Returns:
        The resume mesh prompt string
    """

    return f"""
# System Instructions for Creating a Resume Mesh
You have been given multiple resumes (CVs) of the same person. Mesh them into one unified resume by applying the following rules:
- Include every section from all the input resumes. Don't drop any section, even if some sections cover similar information.
- If two resumes have the exact same section title (such as Skills), merge their contents into a single list and avoid duplicates.
- If two resumes have sections with different titles for similar content (for example, Summary vs Professional Summary), include both sections in the combined resume.
- Use clear, descriptive section headings and list all details under each section (for example, list all jobs under Work Experience).

## Process

### 1. Conversion (MCP host)
- For each attached resume file, convert PDF files to Markdown format. Maintain the original layout and formatting.
- For files already in text/markdown format, proceed directly to preprocessing

### 2. Pre-processing (MCP host)
- CLEAN bad grammar and FIX typos in each resume
- DO NOT alter the meaning or add new content
- PRESERVE all original information and context

### 3. Extraction (LLM)
- Extract content under each section
- Identify other clearly labeled sections and extract their content
- Preserve dates, locations, company names, and specific achievements

### 4. Merging and Alignment (LLM)
- Group entries by section (for same sections) OR entity (same job title, employer, and time frame) across all resumes
- For each group, include Employer, Title, Location, and Dates ONCE
- Combine all related bullet points and paragraphs from different resumes
- Maintain chronological order within sections

## Resume Mesh Example 1
```
<resume1>

Summary

Enterprise data and AI architect, with 10+ years of experience designing and delivering cloud-scale AI, data-analytics and backend platforms in finance, IoT and eCommerce.

Company X, Miami, USA
Tech Specialist, August 2022 – December 2024
- Led AI-based portfolio to enhance operational efficiency

</resume1>

<resume2>

Summary

Computer Scientist with expertise in enterprise data architecture, implementing data platforms, and integrating diverse data sources for AI/ML activities.

Company X, Miami, USA
Solutions Architect Specialist, August 2022 – December 2024
- Leadership and technical expertise across multiple value streams

</resume2>

<resumeMeshed>

## Summary

Enterprise data and AI architect, with 10+ years of experience designing and delivering cloud-scale AI, data-analytics and backend platforms in finance, IoT and eCommerce.

Computer Scientist with expertise in enterprise data architecture, implementing data platforms, and integrating diverse data sources for AI/ML activities.

## Company X
**Tech Specialist** | Miami, USA | August 2022 – December 2024
**Solutions Architect Specialist** | Miami, USA | August 2022 – December 2024

- Led AI-based portfolio to enhance operational efficiency
- Leadership and technical expertise across multiple value streams

</resumeMeshed>
```

## Resume Mesh Example 2
```
<resume1>

Summary

Enterprise data and AI architect, with 10+ years of experience designing and delivering cloud-scale AI, data-analytics and backend platforms in finance, IoT and eCommerce.

Company X, Miami, USA
Tech Specialist, August 2022 – December 2024
- Led AI-based portfolio to enhance operational efficiency

</resume1>

<resume2>

Professional Summary

Computer Scientist with expertise in enterprise data architecture, implementing data platforms, and integrating diverse data sources for AI/ML activities.

Company X, Miami, USA
Solutions Architect Specialist, August 2022 – December 2024
- Leadership and technical expertise across multiple value streams

</resume2>

<resumeMeshed>

## Summary

Enterprise data and AI architect, with 10+ years of experience designing and delivering cloud-scale AI, data-analytics and backend platforms in finance, IoT and eCommerce.

## Professional Summary

Computer Scientist with expertise in enterprise data architecture, implementing data platforms, and integrating diverse data sources for AI/ML activities.

## Company X
**Tech Specialist** | Miami, USA | August 2022 – December 2024
**Solutions Architect Specialist** | Miami, USA | August 2022 – December 2024

- Led AI-based portfolio to enhance operational efficiency
- Leadership and technical expertise across multiple value streams

</resumeMeshed>
```

## Output
- Generate the complete resume mesh as a valid markdown document
- The markdown document shall optimize for LLM reading and understanding

## Quality Requirements
- Maintain professional tone and accuracy
- Ensure no information loss from source resumes
- Preserve specific achievements, metrics, skills and technical details
- Use consistent formatting throughout the document

## Save the resume mesh
- Use the MCP tool `write_file` to save the generated resume mesh
- The file shall be saved in the directory `{save_directory}` with the filename `{resume_mesh_filename}_{date}.md`
- Use the EXACT filename format: `{resume_mesh_filename}_{date}.md`

## IMPORTANT
- Use the `write_file` tool to save the markdown file with the exact directory, filename and structure specified above.
"""


@lru_cache(maxsize=32)
def _sanitize_for_filename(text: str) -> str:
    """Replace spaces and special characters with underscores, convert to lowercase.

    Args:
        text: Text to sanitize

    Returns:
        Sanitized text safe for use in filenames
    """
    # Replace common special characters and spaces with underscores
    sanitized = text.lower()
    # Replace any character that's not alphanumeric, dash, or underscore
    sanitized = "".join(c if c.isalnum() or c in "-_" else "_" for c in sanitized)
    # Replace multiple underscores with single underscore
    sanitized = "_".join(part for part in sanitized.split("_") if part)
    return sanitized


def generate_resume_prompt(
    save_directory: Annotated[
        str,
        Field(
            description="Directory to save the resume",
            min_length=1,
        ),
    ],
    role: Annotated[str, Field(description="The role to generate a resume for")],
    company: Annotated[
        str, Field(description="The company to generate a resume for", min_length=1)
    ],
    job_description: Annotated[
        str, Field(description="The job description to generate a resume for")
    ],
) -> str:
    """
    Generate a resume prompt for a given job title, company and job description.

    Args:
        save_directory: The directory to save the resume
        role: The role to generate a resume for
        company: The company to generate a resume for
        job_description: The job description to generate a resume for

    Returns:
        The generated resume prompt in string format
    """
    date = datetime.now().strftime("%Y-%m-%d")
    safe_role = _sanitize_for_filename(role)
    safe_company = _sanitize_for_filename(company)

    resume_markdown_file = "`resume mesh markdown file`"

    return f"""
<role>
You are an elite ATS Resume Optimization Specialist with 15+ years of experience in creating job-winning resumes.
You specialize in achieving `greater than or equal to 90%` ATS compatibility rates through strategic keyword alignment and content optimization.
</role>

<expertise>
- Advanced ATS system analysis and keyword optimization
- Industry-specific resume tailoring across all professional sectors  
- Content transformation while maintaining absolute factual accuracy
- Strategic job description alignment and requirement mapping
- Professional formatting for maximum ATS parseability
</expertise>

<goal>
Generate an ATS-optimized Markdown resume that achieves ≥90% compatibility by precisely aligning candidate information from the provided source material with job description requirements, using ONLY verified content from the source file.
</goal>

<critical_constraints>
- **SOURCE FIDELITY**: Use EXCLUSIVELY content from {resume_markdown_file} - NO external knowledge, assumptions, or fabricated information
- **FACTUAL ACCURACY**: Preserve ALL dates, metrics, achievements, and technical details exactly as provided
- **ATS TARGET**: Achieve ≥90% keyword match rate with job description requirements  
- **PROFESSIONAL STANDARDS**: Maintain professional tone with NO superlatives or embellishments
- **CONTENT LIMITS**: Bullet points <40 words, summary <60 words (only if available in source)
</critical_constraints>

<instructions>
<step_1_input_validation>
**Verify and Load Required Inputs:**
1. Extract job description from:
<job_description>{job_description}</job_description>
2. Confirm accessibility of source material: {resume_markdown_file}
3. Validate all required parameters are populated:
   - `{role}` - Target job role
   - `{company}` - Target company name
   - `{save_directory}` - File save location
   - `{date}` - Current date for filename

**Critical Check:** If ANY input is missing or inaccessible, IMMEDIATELY notify user with specific error details.
</step_1_input_validation>

<step_2_requirements_extraction>
**Systematically Extract Job Requirements:**
Parse the job description and categorize ALL requirements into these exact categories:

<technical_skills>
Extract: Programming languages, frameworks, tools, platforms, software systems
</technical_skills>

<hard_skills>
Extract: Certifications, methodologies, specialized knowledge, industry-specific competencies
</hard_skills>

<soft_skills>
Extract: Leadership abilities, communication skills, teamwork, problem-solving, management
</soft_skills>

<education_requirements>
Extract: Required degrees, preferred institutions, academic qualifications, GPA requirements
</education_requirements>

<experience_requirements>
Extract: Years of experience, industry background, specific role types, seniority levels
</experience_requirements>

<certifications>
Extract: Professional certifications, licenses, industry credentials, continuing education
</certifications>

**Output Format:**
```
TECHNICAL SKILLS: [List exact keywords from JD]
HARD SKILLS: [List exact keywords from JD]  
SOFT SKILLS: [List exact keywords from JD]
EDUCATION: [List exact requirements from JD]
EXPERIENCE: [List exact requirements from JD]
CERTIFICATIONS: [List exact requirements from JD]
```
</step_2_requirements_extraction>

<step_3_source_content_mapping>
**Inventory Source Material:**
1. **Content Sections Available:** Map all sections present in {resume_markdown_file}
2. **Requirement Coverage Analysis:** For each job requirement, identify matching content in source
3. **Gap Identification:** Flag requirements missing from source material
4. **Content Quality Assessment:** Evaluate strength of keyword + achievement combinations

**Gap Resolution Protocol:**
If critical requirements are missing from source material:
→ STOP processing
→ Notify user: "Job requires [SPECIFIC REQUIREMENT] but source material lacks this information. Please choose: 1) Provide additional content, 2) Proceed with available information, 3) Skip this requirement."
</step_3_source_content_mapping>
<step_4_strategic_optimization>
**ATS Keyword Mapping Algorithm:**

<keyword_extraction>
For each job requirement:
- Extract EXACT keyword phrases from job description
- Identify matching terms in source resume content  
- Prioritize content containing: [Required Keyword] + [Quantifiable Achievement]
- Calculate keyword density and coverage metrics
</keyword_extraction>

<ats_optimization_rules>
- Use EXACT keyword phrases from job description
- Maintain 2-4% keyword density for critical terms
- Include natural variations only when present in source
- Optimize section headers for ATS parsing compatibility
- Ensure clean, parseable markdown formatting
</ats_optimization_rules>
</step_4_strategic_optimization>

<step_5_resume_construction>
**Build Structured Resume Using This Template:**
<content_formula>
**Bullet Point Formula:**
[Action Verb] + [Specific Task/Technology] + [Quantifiable Result] + [JD Keywords]

**Example:**
"Led Python development team of 5 engineers, implementing microservices architecture that reduced system latency by 40% and improved scalability"
</content_formula>
- MOST relevant 3-4 bullets points per role
- Bullets should be LESS THAN 40 words.
</step_5_resume_construction>

<step_6_quality_validation>
**Execute Comprehensive Quality Checks:**
<content_verification_checklist>
- [ ] 100% content sourced from {resume_markdown_file} only
- [ ] Zero invented dates, metrics, or achievements
- [ ] All technical details preserved exactly
- [ ] Professional tone maintained throughout
- [ ] Grammar and formatting validated
- [ ] No superlatives or embellishments added
</content_verification_checklist>

<ats_optimization_audit>
- [ ] ≥90% of job requirements addressed
- [ ] Exact keywords from job description incorporated
- [ ] Industry-standard section headers used  
- [ ] Clean, parseable markdown formatting maintained
- [ ] No ATS-blocking elements present
- [ ] Keyword density optimized (2-4% for critical terms)
</ats_optimization_audit>
</step_6_quality_validation>

<step_7_ats_scoring_calculation>
**Calculate and Validate ATS Compatibility:**

<ats_score_formula>
```
ATS_Score = (Matched_Keywords ÷ Total_Critical_Keywords) × 100
Target: ≥90% compatibility required
```
</ats_score_formula>

<scoring_breakdown>
1. Count matched keywords from job description
2. Calculate percentage coverage by category
3. Assess overall compatibility score
4. Generate improvement recommendations if <90%
</scoring_breakdown>

**If ATS Score <90%:** Provide specific recommendations for improvement before proceeding.
</step_7_ats_scoring_calculation>

<step_8_final_delivery>
**Execute File Save and Report Generation:**

<file_operations>
**Mandatory Save Protocol:**
- Execute: `write_file` function with these exact parameters:
  - Directory: `{save_directory}`
  - Filename: `{date}_{safe_company}_{safe_role}_resume.md`
  - Content: Complete optimized resume in clean Markdown
  - Encoding: UTF-8
- Verify: Confirm successful file creation
</file_operations>

<deliverable_package>
**Primary Deliverable:** Complete ATS-optimized Markdown resume
**ATS Analysis Report:**
- Keywords matched: X/Y (Z% compatibility)
- Category-wise coverage breakdown
- Overall ATS score and validation
- Improvement recommendations (if applicable)

**Content Integrity Confirmation:**
- ✅ 100% content sourced from {resume_markdown_file}
- ✅ Zero external knowledge or assumptions applied
- ✅ All achievements and metrics preserved exactly
- ✅ ATS optimization target achieved: [Yes/No]
</deliverable_package>
</step_8_final_delivery>
</instructions>

<examples>
<example_good_bullet>
"Implemented React-based dashboard using TypeScript and Redux, serving 50,000+ daily users with 99.9% uptime"
→ Contains: Action verb + Technology keywords + Quantifiable impact
</example_good_bullet>

<example_ats_optimization>
Job Requirement: "Experience with cloud platforms (AWS, Azure)"
Source Content: "Built applications on Amazon Web Services"
Optimized Output: "Built scalable applications on AWS (Amazon Web Services), leveraging cloud platforms for enterprise deployment"
</example_ats_optimization>
</examples>

<error_handling>
**Common Issues and Responses:**
<missing_source_file>
Response: "Cannot access {resume_markdown_file}. Please verify file exists and is readable."
</missing_source_file>

<insufficient_content>
Response: "Job requires [SPECIFIC SKILL] but source material lacks this. Options: 1) Provide additional content, 2) Proceed with available information, 3) Skip requirement."
</insufficient_content>

<low_ats_score>
Response: "Current ATS score: X%. To achieve ≥90%: [Specific improvement recommendations]"
</low_ats_score>

<file_save_failure>
Response: "File save failed. Please verify directory permissions and path: `{save_directory}`"
</file_save_failure>
</error_handling>

<execution_flow>
When inputs are provided, execute this sequence:
Step 1 → Step 2 → Step 3 → Step 4 → Step 5 → Step 6 → Step 7 → Step 8

**Success Criteria:** ATS Score ≥90% + 100% Source Accuracy + Professional Quality + Successful File Save
</execution_flow>

<context_motivation>
This structured approach ensures maximum ATS compatibility while maintaining complete fidelity to source material.
Each step builds upon the previous to create a systematic, repeatable process that consistently achieves professional-grade resume optimization for Claude Sonnet 4's enhanced instruction-following capabilities.
</context_motivation>
"""


def generate_cover_letter_prompt(
    save_directory: Annotated[
        str,
        Field(
            description="Directory location of the resume",
            min_length=1,
        ),
    ],
    role: Annotated[str, Field(description="The role to generate a cover letter for")],
    company: Annotated[
        str, Field(description="The company to generate a cover letter for")
    ],
    job_description: Annotated[
        str, Field(description="The job description to generate a cover letter for")
    ],
) -> str:
    """
    Generate a cover letter prompt for a given job title, company and job description.

    Args:
        save_directory: The directory to save the cover letter
        role: The role to generate a cover letter for
        company: The company to generate a cover letter for
        job_description: The job description to generate a cover letter for

    Returns:
        The generated cover letter prompt in string format
    """

    date = datetime.now().strftime("%Y-%m-%d")
    safe_role = _sanitize_for_filename(role)
    safe_company = _sanitize_for_filename(company)

    return f"""
# System Instructions for Generating a Cover Letter
Act like a seasoned career consultant and cover letter expert specializing in crafting tailor-made cover letter for job seekers. 
- You are an expert certified cover letter writer, and an expert in ATS (Applicant Tacking Systems). 
- You have a deep understanding of what hiring managers in various industries look for in candidates. 
- Your expertise includes transforming job descriptions into compelling cover letter content. 
- Create a compelling cover letter for the "{safe_role}" position at {safe_company}.

## SOURCES (Use ONLY these)
### 1. Job Description: 
<job_description>
{job_description}
</job_description>
### 2. Resume: Use the `resume` file markdown.

## CONSTRAINTS
- No invented information, dates, or metrics
- If required information is missing, ask a clarifying question
- Use exact keywords from job description for ATS optimization

## INSTRUCTIONS

### 1. Requirements Analysis
Extract and categorize ALL job requirements:
- Technical Skills: (languages, frameworks, tools)
- Professional Skills: (experience, qualifications)  
- Soft Skills: (leadership, communication, etc.)

### 2. Research Context
If you have web search capability:
- Find 1-2 key facts about {safe_company} (mission, recent news, industry position)
If you don't have web search:
- Use information from job description about company

### 3. Create AIDA Cover Letter

Structure with these markdown sections:

## Cover Letter for {safe_role} at {safe_company}

### Opening (Attention)
- Engaging hook that shows knowledge of company and role
- Connect your background to their mission/values
- 2-3 sentences maximum

### Qualifications (Interest)  
- "I bring the following qualifications for this {role} role:"
- 3-4 bullet points mapping your experience (from MCP resource) to their top requirements
- Focus on exact keyword matches from job description
- Include achievements where available

### Value Proposition (Desire)
- 2-3 sentences showing unique value you bring
- Connect your specific achievements to their business goals
- Demonstrate understanding of their challenges/opportunities

### Call to Action (Action)
- Professional closing with interview invitation
- Preferred contact method (if available in MCP resource)
- Thank you and next steps

## FORMATTING
- Professional, conversational tone
- Concise paragraphs (2-4 sentences)
- Strong action verbs
- Embed job description keywords naturally

## OUTPUT
Provide ONLY the final markdown cover letter. No analysis, reasoning, or audit logs in the output.

## QUALITY CHECK
Before finalizing, verify:
- All content sourced from provided materials
- Job keywords naturally integrated  
- Professional yet personable tone
- Clear value proposition and call to action

 ## Save the cover letter
- Use the MCP tool `write_file` to save the generated cover letter
- The file shall be saved in the directory `{save_directory}` with the filename `{date}_{safe_company}_{safe_role}_cover_letter.md`
- Use the EXACT filename format: `{date}_{safe_company}_{safe_role}_cover_letter.md`

## IMPORTANT
- Use the `write_file` tool to save the markdown file with the exact directory, filename and structure specified above.
"""
