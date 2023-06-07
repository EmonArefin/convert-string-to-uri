def slugify(title):
    slug = title.strip().replace(' ', '-').lower()
    while '--' in slug:
        slug = slug.replace('--', '-')
    return slug


title = input("Enter Your Title: ")
slug = slugify(title)
print(slug)
