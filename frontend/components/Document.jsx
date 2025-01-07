import Image from "next/image";

function Document({ document }) {
  const { name, author, size, createdAt, googleBucketUrl, preview } = document;
  return (
    <>
      <h2 className="text-lg font-bold mb-4">{name}</h2>
      <p className="text-sm text-gray-700 mb-4">Author: {author}</p>
      <p className="text-sm text-gray-700 mb-4">Size: {size}</p>
      <p className="text-sm text-gray-700 mb-4">Created At: {createdAt}</p>
      <p className="text-sm text-gray-700 mb-4">
        Link to the Google Bucket:{" "}
        <a href={googleBucketUrl} target="_blank">
          Preview
        </a>
      </p>
      preview && (
      <Image
        src={preview}
        alt="Document Preview"
        width={500}
        height={500}
        className="w-full h-auto mb-4"
      />
      )
    </>
  );
}

export default Document;
